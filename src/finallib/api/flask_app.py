from datetime import datetime
from flask import Flask, request
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#from finallib.domain import model
from finallib.domain import events
from finallib.adapters import orm
from finallib.service_layer import messagebus, unit_of_work

app = Flask(__name__)
orm.start_mappers()


@app.route("/add_question", methods=["POST"])
def add_question():
    event = events.QuestionCreated(
        request.json["qid"],
        request.json["ques"],
        request.json["aid"],
           )
    messagebus.handle(event, unit_of_work.SqlAlchemyUnitOfWork())
    return "OK", 201


@app.route("/allocate", methods=["POST"])
def allocate_endpoint():
    try:
        event = events.EvaluateRequired(
            request.json["d_id"],
            request.json["dname"]
        )
        results = messagebus.handle(event, unit_of_work.SqlAlchemyUnitOfWork())
        questionqid = results.pop(0)
    except InvalidQues as e:
        return {"message": str(e)}, 400

    return {"questionref": questionqid}, 201
