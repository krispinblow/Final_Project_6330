from __future__ import annotations
from typing import TYPE_CHECKING
from finallib.adapters import email
from finallib.domain import events, model
from finallib.domain.model import DecisionLine

if TYPE_CHECKING:
    from . import unit_of_work


class InvalidQues(Exception):
    pass


def add_question(
    event: events.QuestionCreated,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        answer = uow.answers.get(ques=event.ques)
        if answer is None:
            answer = model.Answer(event.ques, questions=[])
            uow.answers.add(answer)
        answer.batches.append(
            model.Question(event.qid, event.ques, event.aid)
        )
        uow.commit()


def evaluate(
    event: events.EvaluateRequired,
    uow: unit_of_work.AbstractUnitOfWork,
) -> str:
    line = DecisionLine(event.d_id, event.dname)
    with uow:
        answer = uow.answers.get(ques=line.ques)
        if answer is None:
            raise InvalidQues(f"Invalid ques {line.ques}")
        questionqid = answer.allocate(line)
        uow.commit()
        return questionqid


