from __future__ import annotations
from typing import Optional
from datetime import date

from finallib.domain import model
from finallib.domain.model import OrderLine
from finallib.service_layer import unit_of_work
from src.finallib.domain.model import DecisionLine


class InvalidQues(Exception):
    pass


def is_valid_ques(ques, questions):
    return ques in {b.ques for b in questions}


def add_question(
    qid: str, ques: str, aid: str,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        uow.questions.add(model.Question(qid, ques, aid))
        uow.commit()


def evaluate(
    d_id: str, ques: str, aid: str,
    uow: unit_of_work.AbstractUnitOfWork,
) -> str:
    line = DecisionLine(d_id, ques, aid)
    with uow:
        questions = uow.questions.list()
        if not is_valid_ques(line.ques, questions):
            raise InvalidQues(f"Invalid ques {line.ques}")
        questionref = model.evaluate(line, questions)
        uow.commit()
    return questionref