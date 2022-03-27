from datetime import datetime
from flask import Flask, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from finallib.domain import model
from finallib.adapters import orm
from finallib.service_layer import services, unit_of_work

app = Flask(__name__)
orm.start_mappers()


@app.route("/add_question", methods=["POST"])
def add_question():
    """eta = request.json["eta"]
    if eta is not None:
        eta = datetime.fromisoformat(eta).date()"""
    services.add_question(
        request.json["qid"],
        request.json["ques"],
        request.json["aid"],
        # eta,
        unit_of_work.SqlAlchemyUnitOfWork(),
    )
    return "OK", 201


@app.route("/allocate", methods=["POST"])
def allocate_endpoint():
    try:
        questionref = services.allocate(
            request.json["qid"],
            request.json["ques"],
            request.json["aid"],
            unit_of_work.SqlAlchemyUnitOfWork(),
        )
    except (model.OutOfStock, services.InvalidSku) as e:
        return {"message": str(e)}, 400

    return {"questionref": questionref}, 201
