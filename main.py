import pymongo
from pymongo import MongoClient
client = MongoClient()

# db = client.realstate_dev
db2 = client.realstate_dev2

# collection = db.realstate_db
collection2 = db2.realstate_db2

db2.titles.drop()
db2.phones.drop()

titles = db2.titles
phones = db2.phones


# for item in collection2.find().limit(10):     #.skip(2).limit(2):
#   titles.insert_one({"_id": item["_id"], "title": item["title"]})

for item in titles.find():     #.skip(2).limit(2):
  print(item)


# collection2.insert_one({"name": "name 1"})

# import pdb; pdb.set_trace()

