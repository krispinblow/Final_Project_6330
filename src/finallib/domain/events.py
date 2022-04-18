from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

from .models import Evaluate 

class Event(ABC):
    pass


@dataclass
class EvaluateAdded(Event):
    id: int
    teacher_name: str
    club_name: str
    date_added: str


@dataclass
class EvaluateEdited(Event):
    id: int
    teacher_name: str
    club_name: str
    date_edited: str
    

@dataclass
class EvaluateListed(Event):
    bookmarks: List[Evaluate]


