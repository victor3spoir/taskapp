# coding:utf-8

from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

CONNECTION_STRING = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"


def initdb():
    engine = create_engine(CONNECTION_STRING)
    SQLModel.metadata.create_all(engine)
    return engine


def get_session():
    engine = create_engine(CONNECTION_STRING)
    with Session(engine) as session:
        yield session
