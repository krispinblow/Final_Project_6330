import pytest
from src.finallib.adapters import repository
from src.finallib.service_layer import services, unit_of_work


class FakeRepository(repository.AbstractRepository):
    def __init__(self, questions):
        self._questions = set(questions)

    def add(self, question):
        self._questions.add(question)

    def get(self, qid):
        return next(b for b in self._questions if b.qid == qid)
    def list(self):
        return list(self._questions)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.questions = FakeRepository([])
        self.committed = False

    def commit(self):
        self.committed = True

    def rollback(self):
        pass


def test_add_question():
    uow = FakeUnitOfWork()
    services.add_question("2", "Elementary or secondary level?", "2", uow)
    assert uow.questions.get("1") is not None
    assert uow.committed


'''def test_allocate_returns_allocation():
    uow = FakeUnitOfWork()
    services.add_batch("batch1", "COMPLICATED-LAMP", 100, None, uow)
    result = services.allocate("o1", "COMPLICATED-LAMP", 10, uow)
    assert result == "batch1"


def test_allocate_errors_for_invalid_sku():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "AREALSKU", 100, None, uow)

    with pytest.raises(services.InvalidSku, match="Invalid sku NONEXISTENTSKU"):
        services.allocate("o1", "NONEXISTENTSKU", 10, uow)


def test_allocate_commits():
    uow = FakeUnitOfWork()
    services.add_batch("b1", "OMINOUS-MIRROR", 100, None, uow)
    services.allocate("o1", "OMINOUS-MIRROR", 10, uow)
    assert uow.committed'''