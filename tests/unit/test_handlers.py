from __future__ import annotations
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List
import pytest
from finallib import bootstrap
from finallib.domain import commands
from finallib.services import handlers, unit_of_work
from finallib.adapters import repository

from finallib.adapters.orm import start_mappers
from finallib.services.unit_of_work import FakeUnitOfWork


def boostrap_test_app():
    return bootstrap.bootstrap(start_orm=False, uow=FakeUnitOfWork())


def test_add_single_evaluate():

    #arrange
    bus = boostrap_test_app()
    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

    # add one = act
    bus.handle(
        commands.CampusActivityCommand(
            0,
            f"Test",  # teacher_name
            f"test_club",  # club_name
            nu.isoformat(),  # date added
            nu.isoformat(),  # date edited
        )
    )

    print(bus.uow.evaluates.get_by_teacher_name(f"Test"))

    # assert
    assert bus.uow.evaluates.get_by_teacher_name(f"Test") is not None
    assert bus.uow.committed


def test_get_evaluate_by_id():
    bus = boostrap_test_app()

    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

    # add one
    bus.handle(
        commands.CampusActivityCommand(
            99,
            f"Test",  # teacher_name
            f"test_club",  # club_name
            nu.isoformat(),  # date added
            nu.isoformat(),  # date edited
        )
    )

    assert bus.uow.evaluates.get_by_id(99) is not None
    assert bus.uow.committed


def test_get_evaluate_by_club_name():
    bus = boostrap_test_app()

    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

    # add one
    bus.handle(
        commands.CampusActivityCommand(
            99,
            f"Test",  # teacher_name
            f"test_club",  # test_club
            nu.isoformat(),  # date added
            nu.isoformat(),  # date edited
        )
    )

    assert bus.uow.evaluates.get_by_club_name(f"test_club") is not None
    assert bus.uow.committed


def test_get_all_evaluates():
    bus = boostrap_test_app()

    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
    bus.handle(
        commands.CampusActivityCommand(
            99,
            f"Test",  # teacher_name
            f"http://example.com",  # test_club
            nu.isoformat(),  # date added
            nu.isoformat(),  # date edited
        )
    )

    nuto = nu + timedelta(days=2, hours=12)

    bus.handle(
        commands.CampusActivityCommand(
            999,
            f"Test2",  # teacher_name
            f"club_name2",  # test_club
            nuto.isoformat(),  # date added
            nuto.isoformat(),  # date edited
        )
    )

    records = bus.uow.evaluates.get_all()
    assert len(records) == 2



