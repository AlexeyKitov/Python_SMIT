import uvicorn

from api.v1 import insurance
from db.db import init_db
from fastapi import FastAPI

from core.config import conf


app = FastAPI(
    title=conf.fastapi.project_name,
    docs_url=conf.fastapi.docs_url,
    openapi_url=conf.fastapi.openapi_url,
)
init_db(app)

app.include_router(insurance.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=conf.fastapi.fastapi_port,
        reload=conf.fastapi.fastapi_autoreload,
    )
