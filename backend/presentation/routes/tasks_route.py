# coding:utf-8
from uuid import UUID

from fastapi import APIRouter, Depends, responses, status
from sqlmodel import Session

from insfrastructure.db import get_session
from insfrastructure.stores import TasksStore

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])


@router.get("/")
async def get_tasks(session: Session = Depends(get_session)):
    _tasks = await TasksStore(session).get_all()
    return _tasks


@router.get("/{id}")
async def get_task(id: UUID, session: Session = Depends(get_session)):
    _task = TasksStore(session).get(id)
    if not _task:
        return responses.Response(status_code=status.HTTP_404_NOT_FOUND)
    return _task
