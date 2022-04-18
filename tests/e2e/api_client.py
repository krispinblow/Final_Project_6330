import requests
from finallib import config


def post_to_add_evaluate(
    teacher_name: str,
    club_name: str,
    date_added: str,
    date_edited: str,
):
    url = config.get_api_url()

    r = requests.post(
        f"{url}/add_evaluate",
        json={
            "teacher_name": teacher_name,
            "club_name": club_name,
            "date_added": date_added,
            "date_edited": date_edited,
        },
    )
    assert r.status_code == 201


def get_evaluate_by_teacher_name(teacher_name: str):
    club_name = config.get_api_url()
    return requests.get(f"{club_name}/evaluates/{teacher_name}")