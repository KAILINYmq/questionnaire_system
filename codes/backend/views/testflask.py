from flask import Blueprint, jsonify, request, render_template
from config import gssi_col
import pymongo

view = Blueprint('test', __name__)

@view.route("/", methods=["GET"])
def asd():
	return "hello world"

@view.route("/asd", methods=["GET"])
def sdg():
	gssi_col.insert(dict(request.args))
	return render_template('testflask.html', button_name='dsfgv')


company = []

@view.route("/get_company_list", methods=["GET"])
def get_company_list():
	return jsonify(company)

@view.route("/edit_company_info", methods=["POST"])
def edit_company_info():
	global company
	company.append(request.json)
	return f"{len(company)}"

def test_get_and_edit_company():
	import requests

	test_company = {
		"asd": 123451,
		"sdfg": "过去玩恶人"
	}
	requests.post('http://127.0.0.1:5000/test/edit_company_info', json=test_company)
	res = requests.get('http://127.0.0.1:5000/test/get_company_list')
	assert test_company in res.json()

@view.route("/asd", methods=["POST"])
def sdgpost():
	print(request.form)
	return jsonify(request.form)

# GET /asd?srgtsdfg=faesdtq23&srdg=sdgs HTTP/1.1