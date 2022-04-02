from finallib.domain import events
from finallib.domain.model import Answer, DecisionLine, Question






def test_increments_version_number():
    line = DecisionLine("1", "Campus Activity")
    answer = Answer(
        ques="When will the meetings be held?", questions=[Question("q1", "When will the meetings be held?")]
    )
    answer.version_number = 7
    answer.allocate(line)
    assert answer.version_number == 8