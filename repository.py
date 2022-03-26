import abc
import model


class AbstractRepository(abc.ABC):
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
        return self.session.query(model.Question).all()