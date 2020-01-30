from flask import Blueprint, jsonify, request, render_template


import pymongo
from bson import ObjectId
from decimal import Decimal
from config import gssi_col

FixDecimal = Decimal

view = Blueprint(__name__, __name__)


@view.route("/login", methods=["POST", "OPTIONS"])
def login():
    if not request.json:
        return ""
    print(request.json)
    login_id = request.json.get('login_id')
    password = request.json.get('password')
    if login_id and password:
        item = gssi_col.find_one({
            '统一社会信用代码': login_id
        })
        print(item, gssi_col.find_one())
        if item and item['密码'] == password:
            return jsonify({'msg': "登录成功", 'status': 0})
    return jsonify({'msg': "登录失败", 'status': 1})



