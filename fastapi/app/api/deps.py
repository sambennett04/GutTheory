from collections.abc import Generator
from ..db.database import SessionLocal
from fastapi import Depends
from functools import lru_cache
from ..log.log_config import LogConfig
from logging.config import dictConfig
from logging import Logger
from sqlalchemy.orm import Session
from typing import Annotated
from ..util.constants import Constants 

import logging

# database session provider
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[Session, Depends(get_db)]

@lru_cache
def get_logger() -> Logger:
    dictConfig(LogConfig().model_dump())
    return logging.getLogger(Constants.APP_NAME)

LoggerDep = Annotated[Logger, Depends(get_logger)]