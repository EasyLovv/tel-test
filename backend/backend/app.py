"""Application creation."""
import datetime

from bson import ObjectId
from flask import Flask
from flask_restful import Api
from pymongo.cursor import Cursor

from backend import config
from flask_pymongo import PyMongo
import json

mongo = PyMongo()


class JSONEncoder(json.JSONEncoder):
    """The custom JSONEncoder class."""

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return o.timestamp()
        if isinstance(o, Cursor):
            return list(o)
        return super().default(o)


def run():
    from backend import views
    app = Flask(__name__)

    mongo.init_app(app, uri=config.DB_URI)

    api = Api(app)
    api.add_resource(views.Games, '/games')
    api.add_resource(views.DirectGame, '/games/<int:game_id>')

    r_json = app.config.get("RESTFUL_JSON", {})
    r_json["cls"] = app.json_encoder = JSONEncoder
    app.config['RESTFUL_JSON'] = r_json

    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
