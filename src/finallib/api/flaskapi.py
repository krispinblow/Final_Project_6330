from datetime import datetime
from flask import Flask, jsonify, request
from finallib.domain import commands
from finallib import bootstrap

from flask_sqlalchemy import SQLAlchemy

from finallib.adapters.repository import *
from . baseapi import AbstractEvaluateAPI


#from dotenv import load_dotenv
#load_dotenv()

app = Flask(__name__)

class FlaskEvaluateAPI(AbstractEvaluateAPI):
    def __init__(self) -> None:
        super().__init__()
    
    @app.route('/')
    def index(self):
        return f'Final API'

    @app.route('/api/one/<id>')
    def one(self, id):
        return f'The provided id is {id}'

    @app.route('/api/all')
    def all(self):
        return f'all records'

    @app.route('/api/first/<property>/<value>/<sort>')
    def first(self, filter, value, sort):
        return f'the first '
        pass
    
    def many(self, filter, value, sort):
        pass
    
    def add(evaluate):
        pass

    def update(evaluate):
        pass