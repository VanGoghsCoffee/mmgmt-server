from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_envvar('MMGMT_SERVER_CONFIG_FILE')

db = SQLAlchemy(app)

from mmgmt_server.models import Lang, Dish, Recipe, Amount_Unit, Unit, Ingredient

db.create_all()

@app.route('/')
def index():
    return 'Hello'

@app.route('/dish/add', methods=["POST"])
def add_dish():
    print("request: {}".format(request.json["valid"]))
    return jsonify({"result": "ok"})

