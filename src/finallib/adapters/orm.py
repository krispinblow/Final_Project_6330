from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey, events
from sqlalchemy.orm import mapper, relationship

from src.finallib.domain import model


metadata = MetaData()

decision_lines = Table(
    "decision_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("d_id", String(255)),
    Column("dname", String(255)),
)

answers = Table(
    "answers",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("aid", String(255)),
    Column("version_number", Integer, nullable=False, server_default="0"),
)

questions = Table(
    "questions",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("qid", String(255)),
    Column("ques", String(255)),
    Column("aid", String(255)),
)

evaluate = Table(
    "evaluate",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("decisionline_id", ForeignKey("decision_lines.id")),
    Column("question_id", ForeignKey("questions.id")),
)


def start_mappers():
    lines_mapper = mapper(model.DecisionLine, decision_lines)
    questions_mapper = mapper(
        model.Question,
        questions,
        properties={
            "_evaluate": relationship(
                lines_mapper,
                secondary=evaluate,
                collection_class=set,
            )
        },
    )
    mapper(
        model.Answer,
        answers,
        properties={"questions": relationship(questions_mapper)},    
    )

@events.listens_for(model.Answer, "load")
def receive_load(answer, _):
    answer.events =  []