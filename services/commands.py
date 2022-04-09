import sys
from abc import ABC, abstractmethod
from datetime import datetime

import requests

from database import DatabaseManager

# module scope
db = DatabaseManager("evaluates.db")


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("A command must implement the execute method")


class CreateBookmarksTableCommand(Command):
    """
    uses the DatabaseManager to create the evaluates table
    """

    def execute(self, data=None):
        db.create_table(
            "evaluates",
            {
            'id': 'integer primary key autoincrement',
            'teacher_name': 'text not null',
            'club_name': 'text not null',
            'date_added': 'text not null',
            },
        )


class CampusActivityCommand(Command):
       def execute(self, data, timestamp=None):
        data["date_added"] = datetime.utcnow().isoformat()
        db.add("evaluates", data)
        return "Evaluation added!"


class StudentActivityCommand(Command):
    def __init__(self, order_by="date_added"):
        self.order_by = order_by

    def execute(self, data=None):
        return db.select("evaluates", order_by=self.order_by).fetchall()


class EditEvaluateCommand(Command):
    def execute(self, data):
        db.update(
            "evaluates",
            {"id": data["id"]},
            data["update"],
        )
        return "Evaluation updated!"


class QuitCommand(Command):
    def execute(self, data=None):
        sys.exit()