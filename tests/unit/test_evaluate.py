from datetime import date, datetime, timedelta
import random

from finallib.domain import events
from finallib.domain.models import Evaluate

#ok_urls = ["http://", "https://"]

def test_evaluate_teacher_name_is_unique():
    pass

def test_new_evaluate_added_and_edited_times_are_the_same():
    # arrange
    created: str = datetime.now().isoformat()
    
    # act
    edited: str = created
    evaluate = Evaluate(0, "test", "test_club", created, created)

    # assert
    assert evaluate.date_added == evaluate.date_edited

'''def test_new_bookmark_url_is_well_formed():
    # arrange
    created = datetime.now().isoformat()
    edited = created
    
    # act
    bookmark = Bookmark(0, "test", "http://www.example/com", None, created)
    # list comprehensions - https://www.w3schools.com/python/python_lists_comprehension.asp
    okay = [prefix for prefix in ok_urls if bookmark.url.startswith(prefix) ]
    # any function - https://www.w3schools.com/python/ref_func_any.asp
    assert any(okay)'''

def test_that_edit_time_is_newer_than_created_time():
    # arrange
    created: str = datetime.now().isoformat()
    edited: str = created
    
    # act
    evaluate = Evaluate(0, "test", "test", created, edited)

    hours_addition = random.randrange(1,10)
    edit_time = datetime.fromisoformat(evaluate.date_edited)
    evaluate.date_edited = (edit_time + timedelta(hours=hours_addition)).isoformat()

    # assert
    assert evaluate.date_added < evaluate.date_edited