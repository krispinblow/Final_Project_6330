'''from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship
import model

metadata = MetaData()

decision_lines = Table(
    "decision_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("decid", String(255)),
    #Column("qid", Integer, nullable=False),
    #Column("aid", String(255)),
)

answers = Table(
    "answers",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("aid", String(255)),
)

questions = Table(
    "questions",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("qid", String(255)),
    Column("ques", String(255)),
)

evaluations = Table(
    "evaluations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("question_id", ForeignKey("questions.id")),
    Column("answer_id", ForeignKey("answers.id")),
    Column("decisionline_id", ForeignKey("decision_lines.id")),
)

def start_mappers():
    lines_mapper = mapper(model.DecisionLine, decision_lines)
    mapper(
        model.Question,
        questions,
        properties={
            "_evaluations": relationship(
                lines_mapper, secondary=evaluations, collection_class=set,
            )
        },
    )'''