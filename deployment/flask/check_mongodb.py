import pymongo
import datetime
client =pymongo.MongoClient('mongodb://localhost:27017/')
db =client["seg_logs_db"]
col =db['logs']
for x in col.find():
	print(x)
#doc ={'ip': 'test_ip', 'datetime':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'request':'%s %s'%('POST', 'test'), 'img': 'encoded'}
#x =col.insert_one(doc)
