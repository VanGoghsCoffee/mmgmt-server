from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy import exc
import logging

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_envvar('MMGMT_SERVER_CONFIG_FILE')

db = SQLAlchemy(app)
from mmgmt_server.utils.jsonEncoder import CustomJSONEncoder

from mmgmt_server.interactors.database import DatabaseInteractor
from mmgmt_server.interactors.ingredientInteractor import IngredientInteractor
from mmgmt_server.interactors.languageInteractor import LanguageInteractor
from mmgmt_server.utils.rest_answers import write_ok_result

app.json_encoder = CustomJSONEncoder
logger = logging.getLogger('mmgmt_server')
database_interactor = DatabaseInteractor(logger)
ingredient_interactor = IngredientInteractor(logger)
lang_interactor = LanguageInteractor(logger)

@app.route('/')
def index():
    return 'Hello'

@app.route('/dish/add', methods=["POST"])
def add_dish():
    print("request: {}".format(request.json["valid"]))
    return write_ok_result()

@app.route('/ingredient/add', methods=["POST"])
def add_ingredient():
    ingredients_in_db = ingredient_interactor.write_from_json(request.json, db)
    return write_ok_result(ingredients_in_db)

@app.route('/lang/add', methods=["POST"])
def add_lang():
    langs_in_db = lang_interactor.write_from_json(request.json, db)
    return write_ok_result(langs_in_db)

@app.route('/db/reset', methods=["GET"])
def reset_db():
    database_interactor.drop_reset(db)
    return write_ok_result()
