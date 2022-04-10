import pytest
<<<<<<< HEAD
import requests

from src.finallib import config
from ..random_qids import random_ques, random_questionqid, random_d_id



def post_to_add_question(qid, ques, aid):
    url = config.get_api_url()
    r = requests.post(
        f"{url}/add_question", json={"qid": qid, "ques": ques, "aid": aid}
    )
    assert r.status_code == 201


@pytest.mark.usefixtures("postgres_db")
@pytest.mark.usefixtures("restart_api")
def test_happy_path_returns_201_and_evaluated_question():
    ques, otherques = random_ques(), random_ques("other")
    earlyquestion = random_questionqid(1)
    laterquestion = random_questionqid(2)
    otherquestion = random_questionqid(3)
    post_to_add_question(laterquestion, ques, "1")
    post_to_add_question(earlyquestion, ques, "2")
    post_to_add_question(otherquestion, otherques, "1")
    data = {"d_id": random_d_id(), "ques": ques, "aid": "1"}

    url = config.get_api_url()
    r = requests.post(f"{url}/allocate", json=data)

    assert r.status_code == 201
    assert r.json()["questionqid"] == earlyquestion


@pytest.mark.usefixtures("postgres_db")
@pytest.mark.usefixtures("restart_api")
def test_unhappy_path_returns_400_and_error_message():
    unknown_ques, d_id = random_ques(), random_d_id()
    data = {"d_id": d_id, "ques": unknown_ques, "aid": "3"}
    url = config.get_api_url()
    r = requests.post(f"{url}/allocate", json=data)
    assert r.status_code == 400
    assert r.json()["message"] == f"Invalid question {unknown_ques}"
=======

import requests

LOCALHOST = 'http://127.0.0.1:5000/'

def test_api_can_connect():
    res = requests.get(LOCALHOST)
    assert res != None

def test_api_index():
    res = requests.get(LOCALHOST)
    assert res != None
>>>>>>> assign_8a
