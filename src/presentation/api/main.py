from fastapi import FastAPI

from src.infrastructure.config import get_config
from src.infrastructure.redis.main import build_redis
from src.presentation.api.controllers import setup_controllers
from src.presentation.api.di import setup_providers


def create_app(*args) -> FastAPI:
    app = FastAPI()
    settings = get_config()

    redis_pool = build_redis(url=settings.redis.url)
    setup_providers(app, redis_pool=redis_pool)
    setup_controllers(app)

    return app
