from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from core.config import conf

TORTOISE_ORM = {
    "connections": {"default": conf.postgres.get_dsn()},
    "apps": {
        "models": {
            "models": ["api.v1.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def init_db(app) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )


Tortoise.init_models(["api.v1.models"], "models")
