from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING

from finallib.domain import commands, events, models
from src.finallib.domain.commands import EditEvaluateCommand

from src.finallib.domain.events import EvaluateEdited


if TYPE_CHECKING:
    from . import unit_of_work


def add_evaluate(
    cmd: commands.CampusActivityCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        # look to see if we already have this bookmark as the title is set as unique
        evaluate = uow.evaluates.get(title=cmd.title)
        if evaluate is None:
            evaluate = models.Evaluate(
                cmd.teacher_name, cmd.club_name, cmd.date_added, cmd.date_edited
            )
            uow.evaluates.add(evaluate)
        uow.commit()

# ListBookmarksCommand: order_by: str order: str
def list_evaluates(
    cmd: commands.StudentActivityCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        # look to see if we already have this bookmark as the title is set as unique
        evaluate = uow.evaluates.get(title=cmd.title)
        if evaluate is None:
            evaluate = models.Evaluate(
                cmd.teacher_name, cmd.club_name, cmd.date_added, cmd.date_edited
            )
            uow.evaluates.add(evaluate)
        uow.commit()


# EditEvaluateCommand(Command):
def edit_evaluate(
    cmd: commands.EditEvaluateCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        pass


EVENT_HANDLERS = {
    events.CampusActAdded: [add_evaluate],
    events.StudentActAdded: [list_evaluates],
    events.EvaluatesEdited: [edit_evaluate],
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.CampusActivityCommand: add_evaluate,
    commands.StudentActivityCommand: list_evaluates,
    commands.EditEvaluateCommand: edit_evaluate,
}  # type: Dict[Type[commands.Command], Callable]