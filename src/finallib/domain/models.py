from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Evaluate:
     def __init__(self, id, teacher_name, club_name, date_added) -> None:
        self.id = id
        self.teacher_name = teacher_name
        self.club_name = club_name
        self.date_added = date_added
        self.date_edited = self.date_added


'''class EvaluateModel(Base):
    __tablename__ = 'evaluates'

    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(255))
    club_name = Column(String(255))
    date_added = Column(Date)'''