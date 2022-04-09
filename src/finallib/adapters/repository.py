from abc import ABC, abstractmethod

from typing import List, Set

from finallib.adapters import orm
from finallib.domain.models import Base, Evaluate


class AbstractEvaluateRepository(ABC):
    def __init__(self):
        self.evaluates = set()

    @abstractmethod
    def add_one(self,evaluate: Evaluate) -> None:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def add_all(self, evaluates: List[Evaluate]) -> None:
        raise NotImplementedError("Derived classes must implement add_all")

    @abstractmethod
    def get(evaluate: Evaluate, query) -> List[Evaluate]:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def update(evaluate: Evaluate) -> None:
        raise NotImplementedError("Derived classes must implement update")


class SqlAlchemyBookmarkRepository(AbstractEvaluateRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def add_one(self, evaluate: Evaluate) -> None:
        self.session.add(evaluate)
        self.session.commit()

    def add_all(self, evaluates: List[Evaluate]) -> None:
        self.session.add_all(evaluates)
        self.session.commit()

    def get(self, evaluate: Evaluate, query) -> List[Evaluate]:
        pass

    def update(self, evaluate) -> int:
        pass

    def update_many(self, evaluates) -> int:
        pass


class FakeEvaluateRepository(AbstractEvaluateRepository):
    def __init__(self, evaluates):
        super().__init__()
        self._evaluates = set(evaluates)