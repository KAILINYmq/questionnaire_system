from flask import Flask, request, jsonify

app = Flask(__name__)

from views.testflask import view
app.register_blueprint(view, url_prefix='/test')

app.jinja_env.block_start_string = '(%' # 修改块开始符号
app.jinja_env.block_end_string = '%)' # 修改块结束符号
app.jinja_env.variable_start_string = '((' # 修改变量开始符号
app.jinja_env.variable_end_string = '))' # 修改变量结束符号
app.jinja_env.comment_start_string = '(#' # 修改注释开始符号
app.jinja_env.comment_end_string = '#)' # 修改注释结束符号

if __name__ == "__main__":
    app.run(debug=True, port=80)
