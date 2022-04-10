from abc import ABC, abstractmethod
from datetime import datetime

from typing import List, Set

from finallib.adapters import orm
from finallib.domain.models import Evaluate


class AbstractEvaluateRepository(ABC):
    def __init__(self):
        self.seen : set[Evaluate] = set()

    def add(self, evaluate: Evaluate) -> None:
            # add to repo
        self._add(evaluate)
        # add to event list
        self.seen.add(evaluate)

    def get_all(self) -> List[Evaluate]:
        evaluates: List[Evaluate] = self._get_all()
        if evaluates:
            self.seen.update(evaluates)
        return evaluates

    def get_by_id(self, value: int) -> Evaluate:
        # get from repo
        evaluate: Evaluate = self._get_by_id(value)
        if evaluate:
            self.seen.add(evaluate)
        return evaluate 

    def get_by_teacher_name(self, value: str) -> Evaluate:
        # get from repo
        evaluate: Evaluate = self._get_by_teacher_name(value)
        if evaluate:
            self.seen.add(evaluate)
        return evaluate

    def get_by_club_name(self, value: str) -> Evaluate:
        # get from repo
        evaluate: Evaluate = self._get_by_club_name(value)
        if evaluate:
            self.seen.add(evaluate)
        return evaluate


    @abstractmethod
    def _add(self,evaluate: Evaluate) -> None:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def _add_all(self, evaluates: List[Evaluate]) -> None:
        raise NotImplementedError("Derived classes must implement add_all")

    @abstractmethod
    def _get_all(self) -> List[Evaluate]:
        raise NotImplementedError("Derived classes must implement get_all")
    
    @abstractmethod
    def _get_by_id(self, value: int) -> Evaluate:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _get_by_teacher_name(self, value: str) -> Evaluate:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _get_by_club_name(self, value: str) -> Evaluate:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _update(self, evaluate: Evaluate) -> None:
        raise NotImplementedError("Derived classes must implement update")
    
    @abstractmethod
    def _update(self, evaluate: List[Evaluate]) -> None:
        raise NotImplementedError("Derived classes must implement update")


class SqlAlchemyEvaluateRepository(AbstractEvaluateRepository):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def _add(self, evaluate: Evaluate) -> None:
        self.session.add(evaluate)
        self.session.commit()

    def _add_all(self, evaluates: List[Evaluate]) -> None:
        self.session.add_all(evaluates)
        self.session.commit()

    def _get_all(self) -> List[Evaluate]:
        return self.session.query(Evaluate).all()
    
    def _get_by_id(self, value: int) -> Evaluate:
        answer = self.session.query(Evaluate).filter(Evaluate.id == value)
        return answer.one()

    def _get_by_teacher_name(self, value: str) -> Evaluate:
        answer = self.session.query(Evaluate).filter(Evaluate.teacher_name == value)
        return answer.one()

    def _get_by_club_name(self, value: str) -> Evaluate:
        answer = self.session.query(Evaluate).filter(Evaluate.club_name == value)
        return answer.one()    

    def _update(self, evaluate) -> None:
        pass

    def _update(self, evaluates: List[Evaluate]) -> None:
        pass


class FakeEvaluateRepository(AbstractEvaluateRepository):
    def __init__(self, evaluates):
        super().__init__()
        self._evaluates = set(evaluates)
    
    def _add(self, evaluate) -> None:
            self._evaluates.add(evaluate)

    def _add_all(self, evaluates: List[Evaluate]) -> None:
        self._evaluates.update(evaluates)

    def _get_all(self) -> List[Evaluate]:
        return self._evaluates

    
    def _get_by_id(self, value: int) -> Evaluate:
        return next((b for b in self._evaluates if b.id == value), None)

    def _get_by_teacher_name(self, value: str) -> Evaluate:
        return next((b for b in self._evaluates if b.teacher_name == value), None)

    def _get_by_club_name(self, value: str) -> List[Evaluate]:
        return next((b for b in self._evaluates if b.club_name == value), None)

    def _update(self, evaluate: Evaluate) -> None:
        try:
            idx = self._evaluates.index(evaluate)
            bm = self._evaluates[idx]
            with evaluate:
                bm.id = evaluate.id
                bm.teacher_name = evaluate.teacher_name
                bm.club_name = evaluate.club_name
                bm.date_added = evaluate.date_added
                bm.date_edited = datetime.utc.now()
                self._evaluates[idx] = bm
        except:
            self._evaluates.append(evaluate)

        return None

    def _update(self, evaluates: List[Evaluate]) -> None:
        for inbm in evaluates:
            self._update(inbm)