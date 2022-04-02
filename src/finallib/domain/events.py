from dataclasses import dataclass
from typing import Optional


class Event:
    pass


@dataclass
class QuestionCreated(Event):
    qid: str
    ques: str
    aid: str
    

@dataclass
class EvaluateRequired(Event):
    d_id: str
    qid: str
    dname: str
   
@dataclass
class InvalidQues(Event):
    ques: str

