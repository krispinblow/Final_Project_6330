from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Set
import string
from . import events

class Answer:
    def __init__(self, ques: str, questions: List[Question], version_number: int = 0):
        self.ques = ques
        self.questions = questions
        self.version_number = version_number
        self.events = []  # type: List[events.Event]

    def evaluate(self, line: DecisionLine) -> str:
        try:
            question = next(b for b in sorted(self.questions) if b.can_evaluate(line))
            question.evaluate(line)
            self.version_number += 1
            return question.reference
        except StopIteration:
            #self.events.append(events.OutOfStock(line.sku))
            return None

    

@dataclass
class DecisionLine:
    d_id: str
    dname: str
    # doutput: str


"""class AnswerLine:
    aid: str
    answers: str"""


"""def __init__(self) -> None:
        self.raw_text: str = None
        self.Questions = None
        pass"""


class Question:
    def __init__(self, qid: str, ques: str, aid: str):
        self.qid = qid
        self.ques = ques
        self.aid = aid

        self._evaluate = set()  # type Set[DecisionLine]

    def evaluate(self, line: DecisionLine):
        if self.qid == "1" and self.aid == "1":
            return True

    """def can_evaluate(self, line: DecisionLine) -> bool:
        return self.qid == line.qid and self.aid == line.aid"""
