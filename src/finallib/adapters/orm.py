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

from sqlalchemy.orm import registry, mapper, relationship

from ..domain.models import Evaluate

mapper_registry = registry()
Base = mapper_registry.generate_base()

logger = logging.getLogger(__name__)
metadata = mapper_registry.metadata


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
    logger.info("starting mappers")
    mapper_registry.map_imperatively(Evaluate, evaluates)
    
