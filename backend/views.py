from crypt import methods
import imp
from flask import Blueprint
from flask_restful import Api
from flask_cors import CORS

from resource import NoteResource

user_api = Blueprint("api", __name__, url_prefix="/api")
CORS(user_api)

api = Api(user_api)

api.add_resource(NoteResource, "/note", methods=["GET", "POST"])
