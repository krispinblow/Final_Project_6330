import threading
import time
import traceback
from datetime import datetime, timezone
from typing import List
from unittest.mock import Mock
import pytest
from finallib.domain.models import Evaluate
from finallib.services import unit_of_work

# pytestmark = pytest.mark.usefixtures("mappers")

# self.id = id
# self.title = title
# self.url = url
# self.notes = notes
# self.date_added = date_added
# self.date_edited = date_edited
        
def insert_evaluate(session, teacher_name: str, club_name: str, date_added: str, date_edited: str,):
    session.execute(
        """
        INSERT INTO evaluates (teacher_name, club_name, date_added, date_edited) 
        VALUES (:teacher_name, :club_name, :date_added, :date_edited)
        """,
        dict(
            teacher_name=teacher_name, 
            club_name=club_name,
            date_added=date_added,
            date_edited=date_edited,
        ),
    )

def test_can_retreive_evaluate(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
    insert_evaluate(session, f"Test", f"test_club", nu.isoformat(), nu.isoformat())
    session.commit()

    evaluate: Evaluate = None

    uow = unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        evaluate = uow.evaluates.get_by_teacher_name(f"Test")
        assert evaluate.teacher_name == f"Test"
        # uow.commit()

    # assert bookmark.title == f"Test"
