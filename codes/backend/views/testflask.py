from flask import Blueprint, jsonify, request, render_template

from common.ADT import CompanyInfo
from config import company_col
import pymongo
from bson import ObjectId

view = Blueprint('test', __name__)

@view.route("/", methods=["GET"])
def asd():
	return "hello world"

@view.route("/asd", methods=["GET"])
def sdg():
	return render_template('testflask.html', button_name='dsfgv')



@view.route("/get_company_info", methods=["GET"])
def get_company_info():
	item = company_col.find_one({
		"_id": ObjectId(request.json.get('id'))
	})

	return jsonify(item or {})


@view.route("/edit_company_info", methods=["POST"])
def edit_company_info():
	print(list(CompanyInfo.__dict__.keys()), list(request.json.keys()))
	# assert list(CompanyInfo.__dict__.keys()) == list(request.json.keys())
	data: CompanyInfo = request.json

	filter = {'统一社会信用代码': data['统一社会信用代码']}
	item = company_col.find_one(filter)
	if item:
		return jsonify(company_col.update_one(filter, data).raw)
	else:
		return jsonify(company_col.insert_one(data).raw)

def test_edit():
	import requests as req
	item = CompanyInfo(统一社会信用代码=123)


	res = req.post(
		'http://127.0.0.1/test/edit_company_info',
		json=item.__dict__
	)
	assert res.json() == 0
	# res = req.get(
	# 	'http://127.0.0.1/test/get_company_info',
	# 	json={"id": }
	# )