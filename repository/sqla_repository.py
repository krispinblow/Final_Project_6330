from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base_repository import BaseRepository
from ..src.finallib.domain.models import Base, EvaluateModel

class SQLARespository(BaseRepository):
    def __init__(self, club_name=None) -> None:
        super().__init__()

        self.engine = None

        # create db connection
        if club_name != None:
            self.engine = create_engine(club_name)
        else:
            # let's default to in-memory for now
            self.engine = create_engine('sqlite:///:memory:', echo=True)

        # ensure tables are there
        Base.metadata.create_all(self.engine)

        # obtain session
        # the session is used for all transactions
        self.Session = sessionmaker(bind=self.engine)

    def add_one(self, evaluate: EvaluateModel) -> int:
        self.Session.add(evaluate)
        self.Session.commit()
        pass

    def add_many(self, evaluates: List[EvaluateModel]) -> int:
        self.Session.add(evaluates)
        pass

    def update(self, evaluate) -> int:
        pass

    def update_many(self, evaluates) -> int:
        pass

    def find_first(self, query) -> EvaluateModel:
        pass

    def find_all(self, query) -> List[EvaluateModel]:
        pass