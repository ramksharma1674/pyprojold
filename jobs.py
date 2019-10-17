#import sys
import datetime
import cx_Oracle
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#
# Convenience function for getting db column names and assigning an index
#
def getColNames(description):
    fieldNumber = 0;
    fieldNames={}
    for desc in description:
        fieldNames[desc[0]]=fieldNumber
        fieldNumber+=1
    return fieldNames

#
# Return HTML row for STRING values passed
#
def getHtmlRowForEmail(message, jobName, status, startTime, endTime, nextRunTime, dbTime, interval):
    msg = """\
<tr>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
  <td>%s</td>
</tr>
""" % (message, jobName, status, startTime, endTime, nextRunTime, dbTime, interval)
    return msg


print('starting script: ' + str(datetime.datetime.now()))

# Job lookup list
#
# Job Name, Frequency in Minutes, Start Hour
#
jobs = [
        ['Cloud Periodic Purge job', 1440, '12:00:00 PST'],
        ['ACL Clean up job', 1440, '19:00:00 PST'],
        ['Cloud Notification job for SFP', 10, '-1'],
        ['Cloud Notification job', 10, '-1'],
        ['Cloud Periodic Publish job', 60, '-1'],
        ['S3 Suggestion Job', 1440, '00:00:00 PST'],
    ]

#        ['SPRIT Notification Job', 5, '-1'],
# Job arrays to report on later via email
dbJobs = []
unknownStatusJobs = []
successJobs = []
failedJobs = []
pendingLongRunningJobs = []

# Job query
query = """\
SELECT DISTINCT A.JOB_NAME, A.STATUS, A.START_TIME, A.END_TIME, SYSDATE DBDATE
FROM SWC_ADMIN.SWC_JOB_DETAILS A 
WHERE A.JOB_NAME = :str 
  AND A.START_TIME = 
          (SELECT MAX(B.START_TIME) 
           FROM SWC_ADMIN.SWC_JOB_DETAILS B 
           WHERE B.JOB_NAME = A.JOB_NAME)
"""

try:

    #connect to DB
    con = cx_Oracle.connect('SED_READ_ONLY/SED_RE#D0NLY@CSSWPRD')

    for job in jobs:

        jobCursor = con.cursor() 
    
        # setup cursor to get job information
        jobCursor.execute(query, str = job[0])
           
        # get column names to easly index db elements
        colNames = getColNames(jobCursor.description)

        # fetch columns from result set
        for row in jobCursor:

            jobName = row[colNames['JOB_NAME']]
            dbJobs.append(jobName)

            status =row[colNames['STATUS']]
            startTime = row[colNames['START_TIME']]
            endTime = row[colNames['END_TIME']]
            # grabbing current time from the database so it is in the correct timezone
            currentDBTime = row[colNames['DBDATE']]

            # print('currentTime: ' + str(currentTime))
            nextRunTime = startTime + datetime.timedelta(minutes=job[1])

            # is this a status I don't know about?
            if not (status == 'S' or status == 'F' or status == 'P'):
                print('unknown status for job: ' + jobName + ', status: ' + status)
                unknownStatusJobs.append([jobName, status, startTime, endTime, currentDBTime, job[1], job[2], 
                    nextRunTime])
                continue

            # job finished just fine skip to next one
            if status == 'S':
                print('success job: ' + jobName + ', start time: ' + str(startTime)) 
                if (currentDBTime > nextRunTime):
                    successJobs.append([jobName, status, startTime, endTime, currentDBTime, job[1], job[2], 
                        nextRunTime])
                    print('success job: ' + jobName + ' missed the next execution window ' + str(nextRunTime))
                continue

            # job did not finish successfully save and notify
            if status == 'F':
                print('failed job: ' + jobName + ' nextRunTime is ' + str(nextRunTime) + ' and currentTime is ' + 
                   str(currentDBTime))
                failedJobs.append([jobName, status, startTime, endTime, currentDBTime, job[1], job[2], 
                    nextRunTime]) 
                continue

            # job is in progress, check how long it has been running
            if status == 'P':
                print('pending job: ' + jobName + ' nextRunTime is ' + str(nextRunTime) + ' and currentTime is ' + 
                   str(currentDBTime))
                # job should not run past next run time, otherwise it might be running long
                if (currentDBTime > nextRunTime):
                    print('pending job: ' + jobName + ' still running from: ' + str(startTime))
                    pendingLongRunningJobs.append([jobName, status, startTime, endTime, currentDBTime, 
                        job[1], job[2], nextRunTime]) 
                    continue

        # close cursor  to clean up resources
        jobCursor.close()


    con.close()

except cx_Oracle.DatabaseError as e:
    error, = e 
    print(error.code)
    print(error.message)
    quit()


htmlBody = ''

# found that our list locally doesn't match datebase jobs
if (len(dbJobs) != len(jobs)):
    print ('total jobs from DB: ' + str(len(dbJobs)))
    print ('jobs in array to check: ' + str(len(jobs)))
    for job in jobs:
        match = 'N'
        for dbjob in dbJobs:
            if dbjob == job[0]:
                match = 'Y'
                break
        if match == 'N':
            htmlBody += getHtmlRowForEmail('Job Not Found In Database', job[0], 'N/A', 'N/A', 'N/A', 'N/A', 'N/A' ,
                job[1])
            
# found a status that we don't know about
for job in unknownStatusJobs:
    htmlBody += getHtmlRowForEmail('Job Has Unknown Status', job[0], job[1], str(job[2]), str(job[3]), 
        str(job[7]), str(job[4]), str(job[5]))

# found some previously successful jobs that haven't run yet
for job in successJobs:
    htmlBody += getHtmlRowForEmail('Job Past Next Scheduled Run Time', job[0], job[1], str(job[2]), str(job[3]), 
        str(job[7]), str(job[4]), str(job[5]))

# found some failed jobs
for job in failedJobs:
    htmlBody += getHtmlRowForEmail('Failed Job', job[0], job[1], str(job[2]), str(job[3]), str(job[7]), 
        str(job[4]), str(job[5]))

# found some pending jobs that are running past the next scheduled run time
for job in pendingLongRunningJobs:
    htmlBody += getHtmlRowForEmail('Pending Job Running Long', job[0], job[1], str(job[2]), str(job[3]), 
        str(job[7]), str(job[4]), str(job[5]))

#
# Prepare email for each type of job
# 
if (len(htmlBody) > 0):

    SERVER = "outbound.cisco.com"

    FROM = 'itdsscript@itds-script-01.cisco.com'
    TO = ['ramshar@cisco.com']
 #   CC = ['jhasting@cisco.com', 'sbilla@cisco.com','rgoodwin@cisco.com','sasarkar@cisco.com']

    SUBJECT = "WARNING: SWC Jobs Alert - Potential Issues"

    MSG = MIMEMultipart('alternative')
    MSG['Subject'] = SUBJECT
    MSG['From'] = FROM
    MSG['To'] = ', '.join(TO)
 #   MSG['CC'] = ', '.join(CC)

    htmlpre = """\
<html>
  <head>
    <title>
      %s
    </title>
    <style type='text/css'>
      .myTable { background-color:#eee;border-collapse:collapse; }
      .myTable th { background-color:#000;color:white;width:50%%; }
      .myTable td, .myTable th { padding:5px;border:1px solid #000; }
    </style>
  </head>
  <body>
    <br/>
    <h3 style='color:red'>
      %s
    </h3>
    <br/>
    <table class='myTable'>
      <tr>
        <th>Issue</th>
        <th>Job Name</th>
        <th>Status</th>
        <th>Start Time</th>
        <th>End Time</th>
        <th>Next Scheduled Run</th>
        <th>Current DB Time</th>
        <th>Interval in Minutes</th>
      </tr>
""" % (SUBJECT, SUBJECT)

    htmlpost = """\
    </table>
  </body>
</html>
"""

    html = htmlpre + htmlBody + htmlpost

    PART1 = MIMEText(html, 'html')
    MSG.attach(PART1)

    # Send the mail
    sentTo = TO + CC
    server = smtplib.SMTP(SERVER)
    server.sendmail(FROM, sentTo, MSG.as_string())
    server.quit()

print('ending script: ' + str(datetime.datetime.now()))
