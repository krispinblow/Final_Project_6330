from abc import ABC, abstractmethod
from typing import List

from .models import EvaluateModel

class BaseRepository(ABC):

    @abstractmethod
    def add_one(evaluate) -> int:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def add_many(evaluate) -> int:
        raise NotImplementedError("Derived classes must implement add_many")

 

    @abstractmethod
    def update(evaluate) -> int:
        raise NotImplementedError("Derived classes must implement update")

    @abstractmethod
    def update_many(evaluates) -> int:
        raise NotImplementedError("Derived classes must implement update_many")

    @abstractmethod
    def find_first(query) -> EvaluateModel:
        raise NotImplementedError("Derived classes must implement find_first")

    @abstractmethod
    def find_all(query) -> List[EvaluateModel]:
        raise NotImplementedError("Derived classes must implement find_all")
