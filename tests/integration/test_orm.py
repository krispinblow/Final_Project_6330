from src.finallib.domain import model


def test_decisionline_mapper_can_load_lines(session):
    session.execute(
        "INSERT INTO decision_lines (d_id, dname) VALUES "
        '("decision1", "Campus-Activity"),'
        '("decision2", "Student-Activity"),'
        '("decision3", "Not-Activity-Fund")'
    )
    expected = [
        model.DecisionLine("decision1", "Campus-Activity"),
        model.DecisionLine("decision2", "Student-Activity"),
        model.DecisionLine("decision3", "Not-Activity-Fund"),
    ]
    assert session.query(model.DecisionLine).all() == expected


def test_decisionline_mapper_can_save_lines(session):
    new_line = model.DecisionLine("decision1", "Campus-Activity")
    session.add(new_line)
    session.commit()

    rows = list(session.execute('SELECT d_id, dname FROM "decision_lines"'))
    assert rows == [("decision1", "Campus-Activity")]

def test_saving_questions(session):
    question = model.Question("1", "When will meetings be held", "1")
    session.add(question)
    session.commit()
    rows = session.execute(
        'SELECT qid, ques, aid FROM "questions"'
    )
    assert list(rows) == [("1", "When will meetings be held", "1")]