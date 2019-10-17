import cx_Oracle

try:
    con = cx_Oracle.connect('SED_READ_ONLY/SED_RE#D0NLY@CSSWPRD')
    
    crsr = con.cursor()
    crsr.execute("select * from swc_job_owner")
    rs = crsr.fetchall()
    for row in rs:
        print(row)
#        print ("%s, %s " + (row[0], row[1])) 
#    date1 = crsr[fieldNames["sysdate"]]
        #print('Values  -' + date_time)       
    
    crsr.close()
    
    con.close()
    
except cx_Oracle.DatabaseError as e:
    error, = e 
    print(error.code)
    print(error.message)
    quit()
         