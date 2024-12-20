import typing
from uuid import UUID

from sqlmodel import Session, select

from domain.entities import Task


class TasksStore:
    def __init__(self, session: Session) -> None:
        self._session = session
        pass

    async def get_all(self) -> typing.Sequence[Task]:
        query = select(Task)
        _tasks = self._session.exec(query).all()
        return _tasks

    def get(self, id: UUID):
        query = select(Task).where(Task.id == id)
        return self._session.exec(query).first()
