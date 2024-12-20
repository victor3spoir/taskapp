# coding:utf-8
import datetime
from uuid import UUID, uuid4

import sqlmodel
from sqlmodel import Field


class Task(sqlmodel.SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    title: str
    content: str
    created_at: datetime.datetime = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc)
    )
