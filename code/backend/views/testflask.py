from flask import Blueprint, jsonify, request, render_template, make_response, send_from_directory
from config import gssi_col, UPLOAD_PATH, CURRENT_DIR, excel_col, wfjr_col, excel_path, FILE_PATH, FILE_NAME, SHORT_UPLOAD_PATH
from common.ADT_reg import Object, objects, new
from werkzeug.utils import secure_filename
from .Login import admin_JWT
from bson import json_util
from .JWT_token import verify_jwt
import xlrd, os, datetime, math, pprint
import common.验证

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

def excel_JY(data, excel_path, jwt_name):
    """
    获取eccel表值进行验证
    :return:
    """
    # 1.数据格式化
    excel1 = data.sheet_by_index(0)
    excel2 = data.sheet_by_index(1)
    excel1_data = []
    excel2_data = []
    excel1_data_dict = {}
    excel2_data_dict = {}
    try:
        # 1.获取人工成本表
        # for i in range(1, excel1.nrows):
        for i in range(1, 15):
            excel1_data += list(filter(None, excel1.row_values(rowx=i)))
        # 企 业 从 业 人 员 平 均 人 数
        key = list(filter(None, excel1.row_values(rowx=13)))[0]
        data = list(filter(None, excel1.row_values(rowx=13)))[1]
        excel1_data_dict.setdefault(key, data)
        # 在岗人数
        key = list(filter(None, excel1.row_values(rowx=14)))[0]
        data = list(filter(None, excel1.row_values(rowx=14)))[1]
        excel1_data_dict.setdefault(key, data)
        # 企业主要经济指标及企业人工成本指标
        for i in range(20, 35):
            key = list(filter(None, excel1.row_values(rowx=i)))[0]
            data = ''
            try:
                data = list(filter(None, excel1.row_values(rowx=i)))[3]
            except Exception as e:
                data = 1
            excel1_data_dict.setdefault(key, data)
        # 获取{}
        for i in range(0, len(excel1_data), 2):
            excel1_data_dict[excel1_data[i]] = excel1_data[i + 1]
        # 2.获取从业人员表
        for i in range(3, excel2.nrows):
            page_data = {}
            data1 = []
            excel2_data = list(filter(None, excel2.row_values(rowx=i)))
            for j in range(0, 16):
                key = str(list(filter(None, excel2.row_values(rowx=1)))[j]).replace("\n", "")
                try:
                    data1 = excel2_data[j]
                except Exception as e:
                    data1 = 0
                page_data[key] = data1
            excel2_data_dict[str(i)] = page_data
    except Exception as e:
        os.remove(excel_path)
        excel1_data_dict = None
        excel2_data_dict = None
        return excel1_data_dict, excel2_data_dict, None

    try:
        # 3.校验人工成本表数据
        if jwt_name != (str(int(excel1_data_dict["01 统一社会信用代码："]))):
            os.remove(excel_path)
            return None, None, f"上传的统一社会信用代码与登录的账户不符, 期待{jwt_name}, 得到{excel1_data_dict['01 统一社会信用代码：']}"
        common.验证.验证_法人单位名称_错误(excel1_data_dict["02 法人单位名称："])
        common.验证.验证_法定代表人_单位负责人_错误(excel1_data_dict["03 法定代表人 （单位负责人）："])
        common.验证.验证_固话_错误(excel1_data_dict["04 联系方式：固定电话："])
        common.验证.验证_手机_错误(excel1_data_dict["移动电话："])
        common.验证.验证_组织机构代码_错误(excel1_data_dict["组织机构代码："])
        common.验证.验证_企业所在地行政区划代码_错误(excel1_data_dict["05 企业所在地行政区划代码："])
        common.验证.验证_单位隶属关系_错误(excel1_data_dict["06 单位隶属关系(仅限国有单位填写)："])
        common.验证.验证_行业类别代码_错误(excel1_data_dict["07 行业类别代码："])
        common.验证.验证_企业规模_错误(excel1_data_dict["08 企业规模："])
        common.验证.验证_登记注册类型_错误(excel1_data_dict["09 登记注册类型："])
        common.验证.验证_平均人数_错误(excel1_data_dict["10 企 业 从 业 人 员 平 均 人 数："])
        common.验证.验证_在岗人数_错误(excel1_data_dict["      ，其中：（1）在岗职工："])
        common.验证.验证_销售_营业_收入_错误(excel1_data_dict["销售（营业）收入"])
        common.验证.验证_利润总额_错误(excel1_data_dict["利润总额"])
        common.验证.验证_固定资产折旧_错误(excel1_data_dict["固定资产折旧"])
        common.验证.验证_主营业务税金及附加_错误(excel1_data_dict["主营业务税金及附加"])
        common.验证.验证_人工成本总计_错误(excel1_data_dict["人工成本总计"])
        common.验证.验证_从业人员工资总额_错误(excel1_data_dict["从业人员工资总额"])
        common.验证.验证_在岗职工工资总额_错误(excel1_data_dict["    其中：在岗职工工资总额"])
        common.验证.验证_劳务派遣人员工资总额_错误(excel1_data_dict["         劳务派遣人员工资总额"])
        common.验证.验证_福利费用_错误(excel1_data_dict["福利费用"])
        common.验证.验证_教育经费_错误(excel1_data_dict["教育经费"])
        common.验证.验证_保险费用_错误(excel1_data_dict["保险费用"])
        common.验证.验证_劳动保护费用_错误(excel1_data_dict["劳动保护费用"])
        common.验证.验证_住房费用_错误(excel1_data_dict["住房费用"])
        common.验证.验证_其他人工成本_错误(excel1_data_dict["其他人工成本"])
        # 4. 校验从业人员表数据
        for i in range(3, excel2.nrows):
            common.验证.验证_职工代码_错误(excel2_data_dict[str(i)]['职工代码'])
            common.验证.验证_性别_错误(excel2_data_dict[str(i)]['性别'])
            common.验证.验证_出生年份_错误(int(excel2_data_dict[str(i)]['出生年份']))
            common.验证.验证_学历_错误(excel2_data_dict[str(i)]['学历'])
            common.验证.验证_参加工作年份_错误(int(excel2_data_dict[str(i)]['参加工作年份']))
            common.验证.验证_职业_错误(excel2_data_dict[str(i)]['职业'])
            common.验证.验证_管理岗位_专业技术职称_职业技能等级_错误(excel2_data_dict[str(i)]['管理岗位/专业技术职称/职业技能等级'])
            common.验证.验证_用工形式_错误(excel2_data_dict[str(i)]['用工形式'])
            common.验证.验证_劳动合同类型_错误(excel2_data_dict[str(i)]['劳动合同类型'])
            common.验证.验证_全年周平均工作小时数_错误(int(excel2_data_dict[str(i)]['全年周平均工作小时数']))
            common.验证.验证_是否工会会员_错误(excel2_data_dict[str(i)]['是否工会会员'])
            common.验证.验证_全年工资报酬合计_错误(int(excel2_data_dict[str(i)]['全年工资报酬合计']))
            common.验证.验证_基本工资_错误(int(excel2_data_dict[str(i)]['基本工资（类）']))
            common.验证.验证_绩效工资_错误(int(excel2_data_dict[str(i)]['绩效工资（类)']))
            common.验证.验证_津补贴_错误(int(excel2_data_dict[str(i)]['津补贴（类）']))
            common.验证.验证_加班加点工资_错误(int(excel2_data_dict[str(i)]['加班加点工资']))
    except Exception as e:
        excel1_data_dict = None
        excel2_data_dict = None
        return excel1_data_dict, excel2_data_dict, str(e.args)

    # 3.返回数据
    os.remove(excel_path)
    return excel1_data_dict, excel2_data_dict, None

def excel_data_save(excel1_data_dict, excel2_data_dict, jwt_name):
    """
    获取eccel数据入库
    :return:
    """
    # 1.保存数据
    print(excel1_data_dict, excel2_data_dict, jwt_name)
    try:
        wfjr_col.replace_one(
            {"统一社会信用代码": jwt_name},
            {
                "统一社会信用代码": str(int(excel1_data_dict['01 统一社会信用代码：'])),
                "组织机构代码": str(excel1_data_dict['组织机构代码：']),
                "法人单位名称": str(excel1_data_dict['02 法人单位名称：']),
                "法定代表人 （单位负责人）": str(excel1_data_dict['03 法定代表人 （单位负责人）：']),
                "联系方式": {
                    "固话": str(excel1_data_dict['04 联系方式：固定电话：']),
                    "手机": str(excel1_data_dict['移动电话：'])
                },
                "企业所在地行政区划代码": str(excel1_data_dict['05 企业所在地行政区划代码：']),
                "单位隶属关系": str(excel1_data_dict['06 单位隶属关系(仅限国有单位填写)：']),
                "行业类别代码": str(excel1_data_dict['07 行业类别代码：']),
                "企业规模": str(excel1_data_dict['08 企业规模：']),
                "登记注册类型": str(excel1_data_dict['09 登记注册类型：']),
                "企业从业人员平均人数": int(excel1_data_dict['10 企 业 从 业 人 员 平 均 人 数：']),
                "销售（营业）收入": str(excel1_data_dict['销售（营业）收入']),
                "利润总额": str(excel1_data_dict['利润总额']),
                "固定资产折旧": str(excel1_data_dict['固定资产折旧']),
                "主营业务税金及附加": str(excel1_data_dict['主营业务税金及附加']),
                "成本费用总额": str(excel1_data_dict['成本费用总额']),
                "人工成本总计": str(excel1_data_dict['人工成本总计']),
                "从业人员工资总额": str(excel1_data_dict['从业人员工资总额']),
                "福利费用": str(excel1_data_dict['福利费用']),
                "劳务派遣人员工资总额": str(excel1_data_dict['         劳务派遣人员工资总额']),
                "在岗职工工资总额": int(excel1_data_dict['    其中：在岗职工工资总额']),
                "教育经费": str(excel1_data_dict['教育经费']),
                "保险费用": str(excel1_data_dict['保险费用']),
                "劳动保护费用": str(excel1_data_dict['劳动保护费用']),
                "住房费用": str(excel1_data_dict['住房费用']),
                "其他人工成本": str(excel1_data_dict['其他人工成本']),
                "从业人员工资报酬": excel2_data_dict,
            },
            upsert=True
        )
    except Exception as e:
        print(e)
        return False

    # 2.返回数据
    return True



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

# @view.route("/edit_company_info", methods=["POST"])
# def edit_company_info():
#     """
#     管理员编辑/添加公司, 公司信息所指的id存在则进行编辑, 不存在则进行添加
#     :return:
#     """
#     # 2. 验证管理员身份
#     token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODEzMzE3MDAsInVzZXJuYW1lIjoiMSIsInJlZnJlc2giOmZhbHNlfQ.c308l6HYWE4UbQmquvk5A_TpoAnuU60CTgjsvqfh_-E"
#     admin_b = admin_JWT(token)
#     if admin_b == 1:
#         print("管理员操作")
#     elif admin_b == 2:
#         return jsonify({'msg': "请重新登录token过期", 'status': 2})
#     else:
#         print("非法操作")
#     return "123"
    # # assert list(CompanyInfo.__dict__.keys()) == list(request.json.keys())
    # ret = {}
    #
    # data: dict = request.json
    # data: Object = new(objects['CompanyInfo']).from_dict(data)
    # check_ret = data.check()
    # flag = True
    # for item in check_ret:
    #     if 'error' in item.keys():
    #         flag = False
    #         ret['oper_result'] = flag
    #         break
    # if flag:
    #
    #     filter = {'统一社会信用代码': data.get('统一社会信用代码')}
    #     item = gssi_col.find_one(filter)
    #     if item:
    #         ret['oper_result'] = gssi_col.update_one(filter, data).raw
    #     else:
    #         ret['oper_result'] = gssi_col.insert_one(data).raw
    # ret['message'] = check_ret
    # return jsonify(ret)
# def test_edit():
#     objects = Object.read_from('../common/ADT.js')
#
#     import requests as req
#     item = {'asd': 1234}
#
#     res = req.post(
#         'http://127.0.0.1/test/edit_company_info',
#         json=item
#     )
#
#     assert not res.json()['oper_result']
#
#     temp = FixDecimal('100.12')
#     item = {
#         '企业主要经济指标及企业人工成本指标': {
#             "销售（营业）收入": temp,
#             '利润总额': temp,
#             '固定资产折旧': temp,
#             '主营业务税金及附加': temp,
#             '成本费用总额': temp,
#             '人工成本总计': temp,
#             '从业人员工资总额': {
#                 '从业人员工资总额': temp,
#                 '在岗职工工资总额': temp,
#                 '劳务派遣人员工资总额': temp
#             },
#             '福利费用': temp,
#             '教育经费': temp,
#             '保险费用': temp,
#             '劳动保护费用': temp,
#             '住房费用': temp,
#             '其他人工成本': temp,
#         },
#         '从业人员工资报酬信息': [],
#         'had_commited': True
#     }
#     item = new(objects['CompanyInfo']).from_dict(item)
#
#     res = req.post(
#         'http://127.0.0.1/test/edit_company_info',
#         json=item.to_dict()
#     )
#     assert res.json() == False
