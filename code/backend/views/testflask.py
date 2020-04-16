from flask import Blueprint, jsonify, request, render_template, make_response, send_from_directory
from config import gssi_col, UPLOAD_PATH, CURRENT_DIR, excel_col, wfjr_col, excel_path, FILE_PATH, FILE_NAME, SHORT_UPLOAD_PATH
from common.ADT_reg import Object, objects, new
from werkzeug.utils import secure_filename
from .Login import admin_JWT
from bson import json_util
from .JWT_token import verify_jwt
import xlrd, os, datetime, math, pprint
import common.验证
from common.验证 import float_to_str
from common.read_excel import excel_JY, excel_data_save

try:
    objects = Object.read_from(CURRENT_DIR + '/common/ADT.js')
except:
    pass

import pymongo
from bson import ObjectId
from decimal import Decimal

FixDecimal = Decimal

view = Blueprint('test', __name__)

# -----测试---------
@view.route("/", methods=["GET"])
def asd():
    return "hello world"

@view.route("/asd", methods=["GET"])
def sdg():
    return render_template('testflask.html')

#  ----------公用--------------
@view.route("/get_old_sample_table", methods=["GET"])
def get_old_sample_table():
    """
    下载公司历史上传文件
    :return:
    """
    # 1.获取参数校验参数
    data = request.values
    try:
        login_token = data.get('login_token')
    except Exception as e:
        return jsonify({'msg': "参数错误", 'status': 0})
    if not login_token:
        return jsonify({'msg': "参数错误", 'status': 0})

    # 2. 验证登录身份
    jwt_decode = verify_jwt(login_token)
    if not jwt_decode:
        return jsonify({'msg': "请重新登录token过期", 'status': 2})

    # 3.查询数据并返回
    item = excel_col.find({'统一社会信用代码': jwt_decode['username']})
    item1 = excel_path.find_one({'统一社会信用代码': jwt_decode['username']})
    data = []
    for r in item:
        r['file'] = str(item1['path'][1:]+r['file'])
        data.append(json_util.dumps(r))
    return jsonify({'msg': data, 'status': 1})

# ----------用户调用--------------
@view.route("/get_sample_table", methods=["GET"])
def get_sample_table():
    """
    填表者获取用于填写的样例表
    :return: File
    """
    # 1.获取参数校验参数
    data = request.values
    try:
        login_token = data.get('login_token')
    except Exception as e:
        return jsonify({'msg': "参数错误", 'status': 0})
    if not login_token:
        return jsonify({'msg': "参数错误", 'status': 0})

    # 2. 验证登录身份
    jwt_decode = verify_jwt(login_token)
    if not jwt_decode:
        return jsonify({'msg': "请重新登录token过期", 'status': 2})

    # 3. 返回样例表
    try:
        data = make_response(send_from_directory(FILE_PATH, FILE_NAME, as_attachment=True))
        return data
    except Exception as e:
        return jsonify({'msg': "下载异常请稍后重试", 'status': 0})


@view.route("/upload_sample_table", methods=["POST"])
def upload_sample_table():
    """
    填表者上传一个表格并返回是否解析成功
    :return: True
    """
    # 1. 校验参数，用户登录校验
    try:
        login_token = request.values.get('login_token')
        file = request.files.get('file')
    except Exception as e:
        return jsonify({'msg': "参数错误", 'status': 0})
    if not [login_token, file]:
        return jsonify({'msg': "参数错误", 'status': 0})
    jwt_decode = verify_jwt(login_token)
    if not jwt_decode:
        return jsonify({'msg': "请重新登录token过期", 'status': 2})

    # 2. 获取表内数据，验证数据
    filename = secure_filename(file.filename)
    if filename[-4:] != "xlsx":
        return jsonify({'msg': "请上传正确的excel文件", 'status': 0})
    # 2.1 excel暂存short_upload_table文件夹
    filePath = str(int(datetime.datetime.now().timestamp()))+jwt_decode['username']
    filename = filePath+filename
    file.save(os.path.join(SHORT_UPLOAD_PATH, filename))
    # 2.2 获取eccel表值进行验证
    data = xlrd.open_workbook(SHORT_UPLOAD_PATH+filename)
    
    excel1_data_dict, excel2_data_dict, a = excel_JY(data, SHORT_UPLOAD_PATH+filename, jwt_decode['username'])

    if excel1_data_dict is None and excel2_data_dict is None and a is not None:
        return jsonify({'msg': a, 'status': 0})
    # 3. 数据入库，文件存储
    excel_s = excel_data_save(excel1_data_dict, excel2_data_dict, jwt_decode['username'])
    if excel_s is False:
        return jsonify({'msg': "数据存储失败请稍后尝试", 'status': 0})
    # 3.1 文件存储
    path = excel_path.find_one({'统一社会信用代码': jwt_decode['username']})
    if path is not None:
        # 文件储存
        file.save(os.path.join(path['path'], filename))
        excel_col.insert({'统一社会信用代码': jwt_decode['username'],
                            'file': filename, 'time': str(int(datetime.datetime.now().timestamp()))})
    else:
        pp = os.mkdir(UPLOAD_PATH+filePath)
        print(pp)
        excel_path.insert({'统一社会信用代码': jwt_decode['username'],
                                     'path': str(UPLOAD_PATH+filePath+"/")})
        # 文件储存
        file.save(os.path.join(UPLOAD_PATH+filePath, filename))
        excel_col.insert({'统一社会信用代码': jwt_decode['username'],
                            'file': filename, 'time': str(int(datetime.datetime.now().timestamp()))})

    # 4. 返回响应
    return jsonify({'msg': "存储成功", 'status': 1})


@view.route("/get_self_company_info", methods=["POST"])
def get_self_company_info():
    """
    填表者获取本公司的信息返回公司信息类
    :return:
    """
    # 1.获取参数校验参数
    request.get_json(force=True)
    data = request.json
    try:
        login_token = data.get('login_token')
    except Exception as e:
        return jsonify({'msg': "参数错误", 'status': 0})
    if not login_token:
        return jsonify({'msg': "参数错误", 'status': 0})

    # 2. 验证登录身份
    jwt_decode = verify_jwt(login_token)
    if not jwt_decode:
        return jsonify({'msg': "请重新登录token过期", 'status': 2})

    # 3.获取参数返回数据
    item = wfjr_col.find_one({'统一社会信用代码': jwt_decode['username']})
    item = json_util.dumps(item)
    return jsonify({'msg': item, 'status': 1})


# ----------管理员--------------
@view.route("/get_full_state", methods=["GET"])
def get_full_state():
    """
    管理员获取所有公司的填写摘要
    :return:
    """
    # 1. 验证管理员身份
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODEzMzE3MDAsInVzZXJuYW1lIjoiMSIsInJlZnJlc2giOmZhbHNlfQ.c308l6HYWE4UbQmquvk5A_TpoAnuU60CTgjsvqfh_-E"
    admin_b = admin_JWT(token)
    if admin_b == 1:
        print("管理员操作")
    else:
        print("非法操作")
    return "123"

@view.route("/get_company_list", methods=["POST"])
def get_company_list():
    """
    管理员按照页和每页数量获取公司列表
    :return:
    """
    # 1.获取参数校验参数
    request.get_json(force=True)
    data = request.json
    try:
        login_token = data.get('login_token')
        page_size = int(data.get('page_size'))
        page_no = int(data.get('page_no'))
    except Exception as e:
        return jsonify({'msg': "参数错误", 'status': 0})
    if not [login_token, page_size, page_no] and [page_size, page_no] > 0:
        return jsonify({'msg': "参数错误", 'status': 0})

    # 2. 验证管理员身份
    admin_b = admin_JWT(login_token)
    if admin_b == 1:
        print("管理员操作")
    elif admin_b == 2:
        return jsonify({'msg': "请重新登录token过期", 'status': 2})
    else:
        return jsonify({'msg': "非管理员用户", 'status': 0})

    # 3.取出数据返数据
    page_record, page_num = page_query(page_size, page_no)
    data = []
    for r in page_record:
        data.append(json_util.dumps(r))
    return jsonify({'msg': data, 'status': 1, 'page_num': page_num})

def page_query(page_size=10, page_no=1, query_filter=None):
    """
    分页查询
    :return:
    """
    skip = page_size * (page_no - 1)
    page_record = wfjr_col.find(query_filter).limit(page_size).skip(skip)
    page_num = math.ceil(wfjr_col.find(query_filter).count()/page_size)
    return page_record, page_num


@view.route("/get_company_info", methods=["POST"])
def get_company_info():
    """
    管理员获取某个公司的详细信息
    :return:
    """
    # 1.获取参数校验参数
    request.get_json(force=True)
    data = request.json
    try:
        login_token = data.get('login_token')
        id = data.get('id')
    except Exception as e:
        return jsonify({'msg': "参数错误", 'status': 0})
    if not [login_token, id]:
        return jsonify({'msg': "参数错误", 'status': 0})

    # 2. 验证管理员身份
    admin_b = admin_JWT(login_token)
    if admin_b == 1:
        print("管理员操作")
    elif admin_b == 2:
        return jsonify({'msg': "请重新登录token过期", 'status': 2})
    else:
        # 非管理员用户只返回本公司信息
        try:
            jwt_decode = verify_jwt(login_token)
            page_record = wfjr_col.find_one({'统一社会信用代码': jwt_decode['username']})
            data = json_util.dumps(page_record)
            return jsonify({'msg': data, 'status': 1})
        except Exception as e:
            return jsonify({'msg': '查询失败', 'status': 0})

    # 3.查询返回数据
    try:
        page_record = wfjr_col.find_one({"_id": ObjectId(id)})
        data = json_util.dumps(page_record)
        return jsonify({'msg': data, 'status': 1})
    except Exception as e:
        return jsonify({'msg': '查询失败', 'status': 0})

@view.route("/del_company", methods=["POST"])
def del_company():
    """
    管理员删除公司并返回删除结果
    :return:
    """
    # 1.获取参数校验参数
    request.get_json(force=True)
    data = request.json
    try:
        login_token = data.get('login_token')
        id = data.get('id')
    except Exception as e:
        return jsonify({'msg': "参数错误", 'status': 0})
    if not [login_token, id]:
        return jsonify({'msg': "参数错误", 'status': 0})

    # 2. 验证管理员身份
    admin_b = admin_JWT(login_token)
    if admin_b == 1:
        print("管理员操作")
    elif admin_b == 2:
        return jsonify({'msg': "请重新登录token过期", 'status': 2})
    else:
        return jsonify({'msg': "非管理员用户", 'status': 0})

    # 3.删除返回数据
    try:
        page_record = wfjr_col.delete_one({"_id": ObjectId(id)})
        return jsonify({'msg': "删除成功", 'status': 1})
    except Exception as e:
        return jsonify({'msg': "查询删除失败", 'status': 0})

def check_admin(request_json):
    # 1.获取参数校验参数
    request.get_json(force=True)
    data = request_json
    try:
        login_token = data.get('login_token')
        id = data.get('id')
    except Exception as e:
        return {'msg': "参数错误", 'status': 1}
    if not [login_token, id]:
        return {'msg': "参数错误", 'status': 1}

    # 2. 验证管理员身份
    admin_b = admin_JWT(login_token)
    if admin_b == 1:
        print("管理员操作")
    elif admin_b == 2:
        return {'msg': "请重新登录token过期", 'status': 2}
    else:
        return {'msg': "非管理员用户", 'status': 1}
    return {'msg': "非管理员用户", 'status': 0}

@view.route("/add_company", methods=["POST"])
def add_company():
    """
    管理员添加公司
    :return:
    """
    request.get_json(force=True)
    check_admin_ret = check_admin(request.json)
    if check_admin_ret['status'] != 0:
        return jsonify(check_admin_ret)
    ret = {}
    
    data: dict = request.json

    item = {
        "username": data.get('username'),
        "password": data.get('password'),
        "mobile": data.get('mobile'),
        "admin": 0,
        "is_de": 0
    }
    if not (item['username'] and item['password'] and item['mobile']):
        return jsonify({'msg': "参数错误", 'status': 0, 'data': data})
    
    filter = {"username": item['username']}
    find_ret = gssi_col.find_one(filter)
    if find_ret and find_ret.get('admin', 0) != 0:
        return jsonify({'msg': "非法操作, 不可更改管理员", 'status': 0, 'data': data})

    if find_ret:
        gssi_col.replace_one(filter, item)
    else:
        gssi_col.insert_one(item)

    ret['status'] = 1
    return jsonify(ret)