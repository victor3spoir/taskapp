# coding:utf-8

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel

load_dotenv()
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

CONNECTION_STRING = (
    f"postgresql+psycopg2://{DB_PASSWORD}:{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def initdb():
    engine = create_engine(CONNECTION_STRING)
    SQLModel.metadata.create_all(engine)
    return engine


def get_session():
    engine = create_engine(CONNECTION_STRING)
    with Session(engine) as session:
        yield session
