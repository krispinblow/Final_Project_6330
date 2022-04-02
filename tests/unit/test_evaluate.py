from src.finallib.domain.model import DecisionLine, Question


def test_evaluate_decisions():
    question = Question("1", "When are meetings held?", "1")
    line = DecisionLine("1", "Campus-Activity")

    question.evaluate(line)

    # assert Question.aid == "1"

