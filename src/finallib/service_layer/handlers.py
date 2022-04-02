from __future__ import annotations
from typing import TYPE_CHECKING
from finallib.adapters import email
from finallib.domain import commands, events, model
from finallib.domain.model import DecisionLine

if TYPE_CHECKING:
    from . import unit_of_work


class InvalidQues(Exception):
    pass


def add_question(
    cmd: commands.CreateQuestion,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        answer = uow.answers.get(ques=cmd.ques)
        if answer is None:
            answer = model.Answer(cmd.ques, questions=[])
            uow.answers.add(answer)
        answer.questions.append(
            model.Question(cmd.qid, cmd.ques)
        )
        uow.commit()


def evaluate(
    cmd: commands.Evaluate,
    uow: unit_of_work.AbstractUnitOfWork,
) -> str:
    line = DecisionLine(cmd.d_id, cmd.dname)
    with uow:
        answer = uow.answers.get(ques=line.ques)
        if answer is None:
            raise InvalidQues(f"Invalid ques {line.ques}")
        questionqid = answer.evaluate(line)
        uow.commit()
        return questionqid


