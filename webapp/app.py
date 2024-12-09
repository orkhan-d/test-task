from flask import Flask
from db.base import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


@app.route('/ping', methods=['GET'])
def ping():
    return "pong"
