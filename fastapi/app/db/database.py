from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#f creates a format string

user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PW")
netloc = os.environ.get("POSTGRES_NETLOC") or "host.docker.internal"
db = os.environ.get("POSTGRES_DB")

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{netloc}/{db}"

#create SQLAlchemy "engine"(broker b/w application and SQL database)
engine = create_engine(SQLALCHEMY_DATABASE_URL)