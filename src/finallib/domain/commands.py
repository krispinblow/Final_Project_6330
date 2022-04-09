import sys
from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

import requests


class Command(ABC):
    pass

@dataclass
class CampusActivityCommand(Command):
    id: int
    teacher_name: str
    club_name: str
    date_added: str
    date_edited: str

@dataclass 
class StudentActivityCommand(Command):
    id: int
    teacher_name: str
    club_name: str
    date_added: str
    date_edited: str


class EditEvaluateCommand(Command):
    id: int
    teacher_name: str
    club_name: str
    date_added: str
    date_edited: str
