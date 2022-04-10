from datetime import datetime
import json 

from flask import Flask, jsonify, request
from finallib.domain import commands
from finallib.api import views
from finallib import bootstrap



app = Flask(__name__)
bus = bootstrap.bootstrap()

  
@app.route('/')
def index():
    return f'Final API'

@app.route('/add_evaluate', methods=['POST'])
def add_confirm_and_remove_evaluate():
    
    data = request.get_json()
    id = data["id"]
    teacher_name = data["teacher_name"]
    club_name = data["club_name"]
    date_added = data["date_added"]
    date_edited = data["date_edited"]
    
    cmd = commands.CampusActivityCommand(
            id, teacher_name, club_name, date_added, date_edited,
    )
    bus.handle(cmd)
    return "OK", 201


@app.route("/evaluates/<teacher_name>", methods=['GET'])
def get_evaluate_by_teacher_name(teacher_name):
    result = views.evaluates_view(teacher_name, bus.uow)
    if not result:
         return "not found", 404
    return jsonify(result), 200

def get_evaluate_by_id(teacher_name):
    pass

def update(evaluate):
    pass

if __name__ == "__main__":
    app.run()