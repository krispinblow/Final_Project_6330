from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from typing import List

class Evaluate:
     def __init__(self, id, teacher_name, club_name, date_added: datetime, date_edited: datetime):
        self.id : int = id
        self.teacher_name : str = teacher_name
        self.club_name : str = club_name
        self.date_added : str = date_added
        self.date_edited : str = date_edited
        self.events : List[Evaluate]= []


'''class EvaluateModel(Base):
    __tablename__ = 'evaluates'

    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(255))
    club_name = Column(String(255))
    date_added = Column(Date)'''