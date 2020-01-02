from flask import Flask, request, jsonify

app = Flask(__name__)

from views.testflask import view
app.register_blueprint(view, url_prefix='/test')

if __name__ == "__main__":
    app.run(debug=True)
