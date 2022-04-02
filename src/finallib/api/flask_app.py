from datetime import datetime
from flask import Flask, request
from finallib.domain import commands
from finallib.adapters import orm
from finallib.service_layer import messagebus, unit_of_work
from finallib.service_layer.handlers import InvalidQues


app = Flask(__name__)
orm.start_mappers()


@app.route("/add_question", methods=["POST"])
def add_question():
    cmd = commands.CreateQuestion(
        request.json["qid"],
        request.json["ques"],
        request.json["aid"],
           )
    uow = unit_of_work.SqlAlchemyUnitOfWork()
    messagebus.handle(cmd, uow)
    return "OK", 201


@app.route("/allocate", methods=["POST"])
def allocate_endpoint():
    try:
        cmd = commands.Evaluate(
            request.json["d_id"],
            request.json["dname"]
        )
        uow = unit_of_work.SqlAlchemyUnitOfWork()
        results = messagebus.handle(cmd, uow)
        questionqid = results.pop(0)
    except InvalidQues as e:
        return {"message": str(e)}, 400

    return {"questionref": questionqid}, 201
