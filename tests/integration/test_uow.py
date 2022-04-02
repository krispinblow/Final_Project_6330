import threading
import time
import traceback
from typing import List
import pytest
from src.finallib.domain import model
from src.finallib.service_layer import unit_of_work
from ..random_qids import random_ques, random_questionqid, random_d_id


def insert_question(session, qid, ques, answer_version=1):
    session.execute(
        "INSERT INTO answers (ques, version_number) VALUES (:ques, :version)",
        dict(ques=ques,version=answer_version),
    )
    session.execute(
        "INSERT INTO questions (qid, ques) VALUES (:qid, :ques)",
        dict(qid=qid, ques=ques),
    )


def get_evaluated_question_qid(session, d_id, ques):
    [[d_id]] = session.execute(
        "SELECT id FROM decision_lines WHERE d_id=:d_id AND ques=:ques",
        dict(d_id=d_id, ques=ques),
    )
    [[questionqid]] = session.execute(
        "SELECT b.qid FROM allocations JOIN questions AS b ON qid = b.id"
        " WHERE d_id=:d_id",
        dict(d_id=d_id),
    )
    return questionqid


def test_uow_can_retrieve_a_question_and_evaluate_to_it(session_factory):
    session = session_factory()
    insert_question(session, "1", "When will meetings be held?")
    session.commit()

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        answer = uow.questions.get(ques="During class")
        line = model.DecisionLine("1", "Campus Activity")
        answer.evaluate(line)
        uow.commit()

    questionqid = get_evaluated_question_qid(session, "1", "When will meetings be held?")
    assert questionqid == "1"


def test_rolls_back_uncommitted_work_by_default(session_factory):
    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        insert_question(uow.session, "1", "When will meetings be held?")

    new_session = session_factory()
    rows = list(new_session.execute('SELECT * FROM "questions"'))
    assert rows == []


def test_rolls_back_on_error(session_factory):
    class MyException(Exception):
        pass

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with pytest.raises(MyException):
        with uow:
            insert_question(uow.session, "1", "When will meetings be held?")
            raise MyException()

    new_session = session_factory()
    rows = list(new_session.execute('SELECT * FROM "questions"'))
    assert rows == []

def try_to_evaluate(d_id, ques, exceptions):
    line = model.DecisionLine(d_id, ques)
    try:
        with unit_of_work.SqlAlchemyUnitOfWork() as uow:
            answer = uow.answers.get(ques=ques)
            answer.allocate(line)
            time.sleep(0.2)
            uow.commit()
    except Exception as e:
        print(traceback.format_exc())
        exceptions.append(e)


def test_concurrent_updates_to_version_are_not_allowed(postgres_session_factory):
    ques, question = random_ques(), random_questionqid()
    session = postgres_session_factory()
    insert_question(session, question, ques, answer_version=1)
    session.commit()

    answer1, answer2 = random_d_id(1), random_d_id(2)
    exceptions = [] 
    try_to_evaluate_answer1 = lambda: try_to_evaluate(answer1, ques, exceptions)
    try_to_evaluate_answer2 = lambda: try_to_evaluate(answer2, ques, exceptions)
    thread1 = threading.Thread(target=try_to_evaluate_answer1)
    thread2 = threading.Thread(target=try_to_evaluate_answer2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    [[version]] = session.execute(
        "SELECT version_number FROM answers WHERE ques=:ques",
        dict(ques=ques),
    )
    assert version == 2
    [exception] = exceptions
    assert "could not serialize access due to concurrent update" in str(exception)

    answers = session.execute(
        "SELECT d_id FROM allocations"
        " JOIN questions ON allocations.qid = qid.id"
        " JOIN decision_lines ON allocations.decisionline_id = decision_lines.id"
        " WHERE decision_lines.ques=:ques",
        dict(ques=ques),
    )
    assert answers.rowcount == 1
    with unit_of_work.SqlAlchemyUnitOfWork() as uow:
        uow.session.execute("select 1")