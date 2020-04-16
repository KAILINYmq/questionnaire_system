from flask import Flask, request, jsonify
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

from views.testflask import view
app.register_blueprint(view, url_prefix='/test')

from views.Login import view
app.register_blueprint(view, url_prefix='/api')

app.jinja_env.block_start_string = '(%'  # 修改块开始符号
app.jinja_env.block_end_string = '%)'  # 修改块结束符号
app.jinja_env.variable_start_string = '(('  # 修改变量开始符号
app.jinja_env.variable_end_string = '))'  # 修改变量结束符号
app.jinja_env.comment_start_string = '(#'  # 修改注释开始符号
app.jinja_env.comment_end_string = '#)'  # 修改注释结束符号

if __name__ == "__main__":
    CORS(app, supports_credentials=True)
    app.run("0.0.0.0", debug=True, port=8000)
