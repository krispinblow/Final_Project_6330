import os
from datetime import datetime
import sqlite3
import py

import pytest


from services.database import DatabaseManager

@pytest.fixture
def database_manager() -> DatabaseManager:
    filename = "test_evaluates.db"
    dbm = DatabaseManager(filename)
    yield dbm
    dbm.__del__()           # explicitly release the database manager
    os.remove(filename)


def test_database_manager_create_table(database_manager):
    database_manager.create_table(
        "evaluates",
        {
            'id': 'integer primary key autoincrement',
            'teacher_name': 'text not null',
            'club_name': 'text not null',
            'date_added': 'text not null',
        },
    )

    conn = database_manager.connection
    cursor = conn.cursor()

    cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='evaluates' ''')

    assert cursor.fetchone()[0] == 1

    database_manager.drop_table("evaluates")


def test_database_manager_add_evaluate(database_manager):
    database_manager.create_table(
        "evaluates",
        {
            'id': 'integer primary key autoincrement',
            'teacher_name': 'text not null',
            'club_name': 'text not null',
            'date_added': 'text not null',
        },
    )

    data = {
        "teacher_name": "test_name",
        "club_name": "test_club",
        "date_added": datetime.utcnow().isoformat()        
    }

    database_manager.add("evaluates", data)

    conn = database_manager.connection
    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM evaluates WHERE teacher_name='test_name' ''')    
    assert cursor.fetchone()[0] == 1    