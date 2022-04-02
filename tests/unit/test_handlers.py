from datetime import date
from unittest import mock
import pytest

from src.finallib.adapters import repository
from src.finallib.domain import events
from src.finallib.service_layer import handlers, messagebus, unit_of_work


class FakeRepository(repository.AbstractRepository):
    def __init__(self, products):
        super().__init__()
        self._products = set(products)

    def _add(self, product):
        self._products.add(product)

    def _get(self, ques):
        return next((p for p in self._products if p.ques == ques), None)

    def _get_by_questionqid(self, questionqid):
        return next(
            (p for p in self._products for b in p.questions if b.reference == questionqid),
            None,
        )


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    def __init__(self):
        self.products = FakeRepository([])
        self.committed = False

    def _commit(self):
        self.committed = True

    def rollback(self):
        pass


class TestAddBatch:
    def test_for_new_product(self):
        uow = FakeUnitOfWork()
        messagebus.handle(
            events.QuestionCreated("1", "When are meetings held?",), uow
        )
        assert uow.products.get("1") is not None
        assert uow.committed

    '''def test_for_existing_product(self):
        uow = FakeUnitOfWork()
        messagebus.handle(events.BatchCreated("b1", "GARISH-RUG", 100, None), uow)
        messagebus.handle(events.BatchCreated("b2", "GARISH-RUG", 99, None), uow)
        assert "b2" in [b.reference for b in uow.products.get("GARISH-RUG").batches]'''


class TestEvaluate:
    def test_returns_evaluate(self):
        uow = FakeUnitOfWork()
        messagebus.handle(
            events.QuestionCreated("1", "When are meetings held?"), uow
        )
        results = messagebus.handle(
            events.AllocationRequired("1", "When are meetings held?"), uow
        )
        assert results.pop(0) == "1"

    '''def test_errors_for_invalid_sku(self):
        uow = FakeUnitOfWork()
        messagebus.handle(events.BatchCreated("b1", "AREALSKU", 100, None), uow)

        with pytest.raises(handlers.InvalidSku, match="Invalid sku NONEXISTENTSKU"):
            messagebus.handle(
                events.AllocationRequired("o1", "NONEXISTENTSKU", 10), uow
            )'''

    '''def test_commits(self):
        uow = FakeUnitOfWork()
        messagebus.handle(events.BatchCreated("b1", "OMINOUS-MIRROR", 100, None), uow)
        messagebus.handle(events.AllocationRequired("o1", "OMINOUS-MIRROR", 10), uow)
        assert uow.committed'''

    '''def test_sends_email_on_out_of_stock_error(self):
        uow = FakeUnitOfWork()
        messagebus.handle(events.BatchCreated("b1", "POPULAR-CURTAINS", 9, None), uow)

        with mock.patch("allocation.adapters.email.send") as mock_send_mail:
            messagebus.handle(
                events.AllocationRequired("o1", "POPULAR-CURTAINS", 10), uow
            )
            assert mock_send_mail.call_args == mock.call(
                "stock@made.com", f"Out of stock for POPULAR-CURTAINS"
            )'''


'''class TestChangeBatchQuantity:
    def test_changes_available_quantity(self):
        uow = FakeUnitOfWork()
        messagebus.handle(
            events.BatchCreated("batch1", "ADORABLE-SETTEE", 100, None), uow
        )
        [batch] = uow.products.get(sku="ADORABLE-SETTEE").batches
        assert batch.available_quantity == 100

        messagebus.handle(events.BatchQuantityChanged("batch1", 50), uow)

        assert batch.available_quantity == 50

    def test_reallocates_if_necessary(self):
        uow = FakeUnitOfWork()
        event_history = [
            events.BatchCreated("batch1", "INDIFFERENT-TABLE", 50, None),
            events.BatchCreated("batch2", "INDIFFERENT-TABLE", 50, date.today()),
            events.AllocationRequired("order1", "INDIFFERENT-TABLE", 20),
            events.AllocationRequired("order2", "INDIFFERENT-TABLE", 20),
        ]
        for e in event_history:
            messagebus.handle(e, uow)
        [batch1, batch2] = uow.products.get(sku="INDIFFERENT-TABLE").batches
        assert batch1.available_quantity == 10
        assert batch2.available_quantity == 50

        messagebus.handle(events.BatchQuantityChanged("batch1", 25), uow)

        # order1 or order2 will be deallocated, so we'll have 25 - 20
        assert batch1.available_quantity == 5
        # and 20 will be reallocated to the next batch
        assert batch2.available_quantity == 30'''