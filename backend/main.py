# coding:utf-8

from contextlib import asynccontextmanager

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from insfrastructure.db import initdb
from presentation.routes import tasks_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    initdb()
    yield
    print("app shutdown")


app = FastAPI(title="TaskAPI", lifespan=lifespan, docs_url="", redoc_url="")

app.include_router(tasks_route.router)


@app.get("/")
def index():
    return dict(message="Welcome here...")


@app.get("/scalar/v1", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
