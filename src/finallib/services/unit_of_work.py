from __future__ import annotations
from abc import ABC, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


from finallib import config
from finallib.adapters import repository

from finallib.domain.models import Evaluate


class AbstractUnitOfWork(ABC):
    evaluates: repository.AbstractEvaluateRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for evaluate in self.evaluates.seen:
            while evaluate.events:
                yield evaluate.events.pop(0)

    @abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_sqlite_file_url(),
        isolation_level="SERIALIZABLE",
    )
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.evaluates = repository.SqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

class FakeUnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.evaluates = repository.FakeEvaluateRepository(evaluates = [])
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass