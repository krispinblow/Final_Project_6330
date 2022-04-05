from model import DecisionLine, Question, Answer, choices

def test_evaluate_input():
    qid1 = input(f'When are meetings held? {choices}:')
    line = DecisionLine("dec1")
    
    qid1.evaluate(line)
    
    assert choices == "B"

    