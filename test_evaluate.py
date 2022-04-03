from model import DecisionLine, Question, Answer

def test_evaluate_input():
    qid1 = aid1
    line = Answer("aid1")
    
    qid1.evaluate(line)
    
    assert DecisionLine == "dec1"

    