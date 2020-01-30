from flask import Blueprint, jsonify, request, render_template
from config import gssi_col, CURRENT_DIR
from common.ADT_reg import Object, objects, new

try:
    objects = Object.read_from(CURRENT_DIR + '/common/ADT.js')
except:
    pass

import pymongo
from bson import ObjectId
from decimal import Decimal

FixDecimal = Decimal

view = Blueprint('test', __name__)


@view.route("/", methods=["GET"])
def asd():
    return "hello world"


@view.route("/asd", methods=["GET"])
def sdg():
    return render_template('testflask.html')

count = 1
@view.route("/get_company_info", methods=["GET"])
def get_company_info():
    global count
    item = gssi_col.find_one({
        "_id": ObjectId(request.args.get('id'))
    })
    count += 1
    return jsonify({"asd": count})
    return jsonify(item or {})


@view.route("/edit_company_info", methods=["POST"])
def edit_company_info():
    # assert list(CompanyInfo.__dict__.keys()) == list(request.json.keys())
    ret = {}

    data: dict = request.json
    data: Object = new(objects['CompanyInfo']).from_dict(data)
    check_ret = data.check()
    flag = True
    for item in check_ret:
        if 'error' in item.keys():
            flag = False
            ret['oper_result'] = flag
            break
    if flag:

        filter = {'统一社会信用代码': data.get('统一社会信用代码')}
        item = gssi_col.find_one(filter)
        if item:
            ret['oper_result'] = gssi_col.update_one(filter, data).raw
        else:
            ret['oper_result'] = gssi_col.insert_one(data).raw
    ret['message'] = check_ret
    return jsonify(ret)


def test_edit():
    objects = Object.read_from('../common/ADT.js')

    import requests as req
    item = {'asd': 1234}

    res = req.post(
        'http://127.0.0.1/test/edit_company_info',
        json=item
    )

    assert not res.json()['oper_result']

    temp = FixDecimal('100.12')
    item = {
        '企业主要经济指标及企业人工成本指标': {
            "销售（营业）收入": temp,
            '利润总额': temp,
            '固定资产折旧': temp,
            '主营业务税金及附加': temp,
            '成本费用总额': temp,
            '人工成本总计': temp,
            '从业人员工资总额': {
                '从业人员工资总额': temp,
                '在岗职工工资总额': temp,
                '劳务派遣人员工资总额': temp
            },
            '福利费用': temp,
            '教育经费': temp,
            '保险费用': temp,
            '劳动保护费用': temp,
            '住房费用': temp,
            '其他人工成本': temp,
        },
        '从业人员工资报酬信息': [],
        'had_commited': True
    }
    item = new(objects['CompanyInfo']).from_dict(item)

    res = req.post(
        'http://127.0.0.1/test/edit_company_info',
        json=item.to_dict()
    )
    assert res.json() == False
