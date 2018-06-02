import pymongo


client = pymongo.MongoClient(host='localhost', port=27017)
db = client.weibo
collection = db.weibo
condition = {'account_id': 1757335345}
result = collection.find(condition).count()
print(result)

# result = collection.remove(condition)
# print(result)
