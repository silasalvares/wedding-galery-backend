import os
from flask import Flask
from flask_cors import CORS

webapi = Flask(__name__)
CORS(webapi)

from dotenv import load_dotenv
load_dotenv('.env')

from mongoengine import connect
connect(os.environ.get('MONGO_DB'), host=os.environ.get('MONGO_HOST'))

from .api import api
webapi.register_blueprint(api)