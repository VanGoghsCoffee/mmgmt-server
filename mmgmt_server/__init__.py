from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import logging


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_envvar('MMGMT_SERVER_CONFIG_FILE')
db = SQLAlchemy(app)

from mmgmt_server.interactors.languageInteractor import LanguageInteractor

logger = logging.getLogger('model')
lang_interactor = LanguageInteractor(logger)


def write_ok_result(payload=""):
    result = {
        "result": "ok",
        "payload": payload
    }
    return jsonify(result)

@app.route('/')
def index():
    return 'Hello'

@app.route('/dish/add', methods=["POST"])
def add_dish():
    print("request: {}".format(request.json["valid"]))
    return jsonify({"result": "ok"})

@app.route('/lang/add', methods=["POST"])
def add_lang():
    lang_interactor.write_from_json(request.json, db)
    return write_ok_result(request.json)

