import os
from logging import config as logging_config

from pydantic import Field, BaseModel, BaseSettings

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)


class ConfFastApi(BaseSettings):
    fastapi_autoreload: bool = Field(True, env="FASTAPI_AUTORELOAD")
    project_name: str = Field("Python_SMIT", env="PROJECT_NAME")
    docs_url: str = "/api/openapi"
    openapi_url: str = "/api/openapi.json"
    base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fastapi_port: int = Field(8001, env="FASTAPI_PORT")
    fastapi_host: str = Field("127.0.0.1", env="FASTAPI_HOST")

    class Config:
        env_file = ".env"


class ConfPostgres(BaseSettings):
    host: str = Field("127.0.0.1", env="DB_HOST")
    port: int = Field(5432, env="DB_PORT")
    db: str = Field("postgres_db_name", env="POSTGRES_DB")
    user: str = Field("postgres_user", env="POSTGRES_USER")
    password: str = Field("postgres_password", env="POSTGRES_PASSWORD")
    batch_size: int = Field(100, env="BATCH_SIZE")

    class Config:
        env_file = ".env"

    def get_dsn(self):
        return (
            f"postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"
        )


class Conf(BaseModel):
    postgres: BaseSettings = ConfPostgres()
    fastapi: BaseSettings = ConfFastApi()


conf = Conf()
