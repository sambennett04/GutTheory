from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
netloc = os.environ.get("POSTGRES_NETLOC") or "host.docker.internal"
db = os.environ.get("POSTGRES_DB")

#f creates a format string
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{netloc}/{db}"

#create SQLAlchemy "engine"(broker b/w application and SQL database)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create a session that uses the database engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()