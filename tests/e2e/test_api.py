from datetime import datetime, timezone
from random import *

from .api_client import post_to_add_evaluate, get_evaluate_by_teacher_name
import pytest

from finallib import config


@pytest.mark.usefixtures("file_sqlite_db")
# @pytest.mark.usefixtures("restart_api")
@pytest.mark.usefixtures("client")
def test_path_correct_returns_201_and_evaluate_added(client):

    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

    id=randint(1,1000)
    teacher_name = f"Test"
    club_name = f"test_club"
    date_added = nu.isoformat()
    date_edited = nu.isoformat()

    # post_to_add_evaluate(title, url, notes, date_added, date_edited)
    club_name = config.get_api_url()

    r = client.post(
        "/add_evaluate",
        json={
            "id": id,
            "teacher_name": teacher_name,
            "club_name": club_name,
            "date_added": date_added,
            "date_edited": date_edited,
        },
    )

    assert r.status_code == 201

    # r = client.post(
    #     f"{url}/add_bookmark",
    #     json={
    #         "title": title,
    #         "url": url,
    #         "notes": notes,
    #         "date_added": date_added,
    #         "date_edited": date_edited,
    #     },
    # )

    # r = get_bookmark_by_title(title)
    # assert r.ok
    # assert r.json() == [
    #     {
    #         "title": title,
    #         "url": url,
    #         "notes": notes,
    #     },
    # ]


# @pytest.mark.usefixtures("file_sqlite_db")
# @pytest.mark.usefixtures("restart_api")
# def test_incorrect_path_returns_400_and_error_message():

#     nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

#     title: str = f"Test"
#     url: str = f"http://example.com"
#     notes: str = f"good links"
#     date_added: str = nu.isoformat()
#     date_edited: str = nu.isoformat()
#     r = post_to_add_bookmark(title, url, notes, date_added, date_edited)
#     assert r.status_code == 400
#     assert r.json()["message"] == f"Invalid title {title}"

#     r = get_bookmark_by_title(title)
#     assert r.status_code == 404







'''import pytest

import requests

LOCALHOST = 'http://127.0.0.1:5000/'

def test_api_can_connect():
    res = requests.get(LOCALHOST)
    assert res != None

def test_api_index():
    res = requests.get(LOCALHOST)
    assert res != None'''