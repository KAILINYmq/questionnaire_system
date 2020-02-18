import pymongo

# JWT加密
JWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'
# JWT有效期两小时
JWT_EXPIRY_HOURS = 2
# 公司下载excel路径
FILE_PATH = "./file/"
FILE_NAME = "style_sheet.xlsx"
# excel暂时存储路径
SHORT_UPLOAD_PATH = "./short_upload_table/"
# excel存储路径
UPLOAD_PATH = "./upload_table/"

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["questionnaire_system"]
collist = db.list_collection_names()
# if not "wfjr" and "gssi" in collist:
wfjr_col = db["message"]
gssi_col = db["users"]
excel_col = db["excel_url"]
excel_path = db["path"]


import os
CURRENT_DIR = os.getcwd()