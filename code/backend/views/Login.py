from flask import Blueprint, render_template, request
from flask.json import jsonify
import flask_login
import pymongo
from bson import ObjectId
from decimal import Decimal
from config import gssi_col, JWT_EXPIRY_HOURS
from datetime import datetime, timedelta
from .JWT_token import generate_jwt, verify_jwt

FixDecimal = Decimal

view = Blueprint(__name__, __name__)

def _generate_tokens(username):
    """
    生成token
    :param username: username
    :return: token
    """
    # 颁发JWT
    now = datetime.utcnow()
    expiry = now + timedelta(hours=JWT_EXPIRY_HOURS)
    token = generate_jwt({'username': username, 'refresh': False}, expiry)
    return token

@view.route("/login", methods=["POST"])
def login():
    """
    登录
    :return: login_token
    """
    # 1.获取参数
    request.get_json(force=True)
    data = request.json
    username = data.get('username')
    password = data.get("password")

    # 2.校验参数返回数据
    if not all([username, password]):
        return jsonify({'msg': "参数错误", 'status': 0})
    item = gssi_col.find_one({'username': username})
    if item is None:
        return jsonify({'msg': "登录失败！", 'status': 0})
    if item['admin'] == 1:
        if item["password"] == password:
            token = _generate_tokens(username)
            return jsonify({'msg': "admin登录成功", 'login_token': token})
    else:
        if item["password"] == password:
            token = _generate_tokens(username)
            return jsonify({'msg': "登录成功", 'login_token': token})

    return jsonify({'msg': "账号或密码错误，登录失败！", 'status': 0})


def admin_JWT(token):
    """
    验证JWT是否是管理员
    :return:
    """
    jwt_decode = verify_jwt(token)
    if not jwt_decode:
        return 2
    item = gssi_col.find_one({'username': jwt_decode['username']})
    if item['admin'] == 1:
        return 1
    else:
        return 0