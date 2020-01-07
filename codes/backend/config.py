import pymongo
 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]
wfjr_col = db["wfjr"]
company_col = db["gssi"]

import os
CURRENT_DIR = os.getcwd()