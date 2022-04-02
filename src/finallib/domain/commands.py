from typing import Optional
from dataclasses import dataclass


class Command:
    pass


@dataclass
class Evaluate(Command):
    d_id: str
    ques: str
    aid: str


@dataclass
class CreateQuestion(Command):
    qid: str
    ques: str


