import pymongo
client =pymongo.MongoClient('mongodb://localhost:27017/')
db =client["seg_logs_db"]
col =db['logs']
for x in col.find():
	print(x)
# doc ={'ip': request.remote_addr, 'datetime':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'request':'%s %s'%(request.method, request.url), 'img': encoded}
# x =col.insert_one(doc)
