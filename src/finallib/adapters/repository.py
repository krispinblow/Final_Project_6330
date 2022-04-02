import abc
from typing import Set
from src.finallib.adapters import orm
from src.finallib.domain import model

class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()  # type: Set[model.Product]

    def add(self, answer: model.Answer):
        self._add(answer)
        self.seen.add(answer)

    def get(self, ques) -> model.Answer:
        answer = self._get(ques)
        if answer:
            self.seen.add(answer)
        return answer

    def get_by_questionqid(self, questionqid) -> model.Answer:
        answer = self._get_by_questionqid(questionqid)
        if answer:
            self.seen.add(answer)
        return answer

    @abc.abstractmethod
    def _add(self, answer: model.Answer):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, ques) -> model.Answer:
        raise NotImplementedError

    @abc.abstractmethod
    def _get_by_questionqid(self, questionqid) -> model.Answer:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _add(self, answer):
        self.session.add(answer)

    def _get(self, ques):
        return self.session.query(model.Answer).filter_by(ques=ques).first()

    def _get_by_questionqid(self, questionqid):
        return (
            self.session.query(model.Answer)
            .join(model.Question)
            .filter(orm.questions.c.reference == questionqid)
            .first()
        )
'''class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, question: model.Question):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, qid) -> model.Question:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, question):
        self.session.add(question)

    def get(self, qid):
        return self.session.query(model.Question).filter_by(qid=qid).one()

    def list(self):
        return self.session.query(model.Question).all()'''
