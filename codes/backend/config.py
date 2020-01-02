import pymongo
 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]
wfjr_col = db["wfjr"]
gssi_col = db["gssi"]
