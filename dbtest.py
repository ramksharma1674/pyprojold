from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb://entitlement_user:mongo123@mngdb-ebf-stg-01.cisco.com:27048/entitlement_db')
db=client['entitlement_db']
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
i = 0
result = db.powerUsers.find()
for document in result:
    i = i+1
    
print (i)