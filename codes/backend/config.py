import pymongo
 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["questionnaire_system"]
wfjr_col = db["wfjr"]
gssi_col = db["gssi"]

import os
CURRENT_DIR = os.getcwd()