from src.finallib.adapters import repository
from src.finallib.domain import model

def test_get_by_questionqid(session):
    repo = repository.SqlAlchemyRepository(session)
    q1 = model.Question(qid="1", ques="When will meetings be held?", aid="1")
    q2 = model.Question(qid="2", ques="Elmentary or Secondary?", aid="2")
    q3 = model.Question(qid="3", ques="STUCO?", aid="1")
    a1 = model.Answer(ques="When will meetings be held?", questions=[q1])
    a2 = model.Answer(ques="Elmentary or Secondary?", questions=[q2])
    a3 = model.Answer(ques="STUCO?", questions=[q3])
    repo.add(a1)
    repo.add(a2)
    repo.add(a3)
    assert repo.get_by_questionqid("q1") == a1
    assert repo.get_by_questionqid("q2") == a2
    assert repo.get_by_questionqid("q3") == a3

