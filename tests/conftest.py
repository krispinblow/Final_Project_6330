import time
from pathlib import Path

import pytest
import requests
from requests.exceptions import ConnectionError
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers

from finallib.adapters.orm import metadata, start_mappers
from finallib import config
from finallib.api import flaskapi

pytest.register_assert_rewrite("tests.e2e.api_client")


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def sqlite_session_factory(in_memory_sqlite_db):
    yield sessionmaker(bind=in_memory_sqlite_db)


@pytest.fixture
def mappers():
    start_mappers()
    yield
    clear_mappers()


@retry(stop=stop_after_delay(10))
def wait_for_sqlite_to_come_up(engine):
    return engine.connect()


@retry(stop=stop_after_delay(10))
def wait_for_postgres_to_come_up(engine):
    return engine.connect()


@retry(stop=stop_after_delay(10))
def wait_for_webapp_to_come_up():
    return requests.get(config.get_api_url())


@retry(stop=stop_after_delay(10))
def wait_for_redis_to_come_up():
    r = redis.Redis(**config.get_redis_host_and_port())
    return r.ping()


@pytest.fixture(scope="session")
def file_sqlite_db():
    engine = create_engine(config.get_sqlite_file_url(), isolation_level="SERIALIZABLE")
    wait_for_sqlite_to_come_up(engine)
    metadata.create_all(engine)
    return engine   


@pytest.fixture(scope="session")
def postgres_db():
    engine = create_engine(config.get_postgres_uri(), isolation_level="SERIALIZABLE")
    wait_for_postgres_to_come_up(engine)
    metadata.create_all(engine)
    return engine


@pytest.fixture
def postgres_session_factory(postgres_db):
    yield sessionmaker(bind=postgres_db)


@pytest.fixture
def postgres_session(postgres_session_factory):
    return postgres_session_factory()


@pytest.fixture
def client():
    flaskapi.app.config['TESTING'] = True
    return flaskapi.app.test_client()


@pytest.fixture
def restart_api():
    fa = Path(__file__).parent.parent / "src/finallib/api/flaskapi.py"
    print(fa)
    fa.touch()
    time.sleep(0.5)
    wait_for_webapp_to_come_up()


@pytest.fixture
def restart_redis_pubsub():
    wait_for_redis_to_come_up()
    if not shutil.which("docker-compose"):
        print("skipping restart, assumes running in container")
        return
    subprocess.run(
        ["docker-compose", "restart", "-t", "0", "redis_pubsub"],
        check=True,
    )
