import pytest
from src.finallib.domain import model
from src.finallib.service_layer import unit_of_work


def insert_question(session, qid, ques, aid):
    session.execute(
        "INSERT INTO questions (qid, ques)"
        " VALUES (:qid, :ques, :aid)",
        dict(qid=qid, ques=ques, aid=aid),
    )


def get_evaluated_question_qid(session, d_id, ques):
    [[d_id]] = session.execute(
        "SELECT id FROM decision_lines WHERE d_id=:d_id AND ques=:ques",
        dict(d_id=d_id, ques=ques),
    )
    [[questionqid]] = session.execute(
        "SELECT b.qid FROM allocations JOIN questions AS b ON question_id = b.id"
        " WHERE d_id=:d_id",
        dict(d_id=d_id),
    )
    return questionqid


def test_uow_can_retrieve_a_question_and_evaluate_to_it(session_factory):
    session = session_factory()
    insert_question(session, "1", "When will meetings be held?", "1")
    session.commit()

    uow = unit_of_work.SqlAlchemyUnitOfWork(session_factory)
    with uow:
        question = uow.questions.get(reference="1")
        line = model.DecisionLine("1", "Campus Activity")
        question.evaluate(line)
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