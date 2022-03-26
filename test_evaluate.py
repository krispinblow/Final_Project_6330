from model import DecisionLine, AnswerLine, Question

def test_evaluate_decisions():
    question = Question("1", "When are meetings held?", "1")
    line = DecisionLine("1", "1")
    
    question.evaluate(line)
    
    assert question.aid == "1"

    