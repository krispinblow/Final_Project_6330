import logging
from typing import Text
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    event,
)

from sqlalchemy.orm import mapper

from ..domain.models import Evaluate

logger = logging.getLogger(__name__)

metadata = MetaData()


evaluates = Table(
    "evaluates",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("teacher_name", String(255), unique=True),
    Column("club_name", String(255)),
    Column("date_added", DateTime),
    Column("date_edited", DateTime),
)


def start_mappers():
    logger.info("string mappers")
    evaluates_mapper = mapper(Evaluate, evaluates)