# pylint: disable=protected-access
import model
import repository


def test_repository_can_save_a_question(session):
    question = model.Question("1", "When are meetings held?", "1")

    repo = repository.SqlAlchemyRepository(session)
    repo.add(question)
    session.commit()

    rows = session.execute(
        'SELECT qid, ques, aid FROM "questions"'
    )
    assert list(rows) == [("1", "When are meetings held?", "1")]


def insert_decision_lines(session):
    session.execute(
        "INSERT INTO decision_lines (d_id, dname)"
        ' VALUES ("1", "Campus Activity")'
    )
    [[decisionline_id]] = session.execute(
        "SELECT id FROM decision_lines WHERE d_id=:d_id AND dname=:dname",
        dict(d_id="1", dname="Campus Activity"),
    )
    return decisionline_id


