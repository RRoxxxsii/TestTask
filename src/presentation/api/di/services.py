from fastapi import Depends

from src.domain.usecases.main import Interactor
from src.infrastructure.redis.service import RedisService
from src.presentation.api.di import get_aioredis


def get_service(redis: RedisService = Depends(get_aioredis)) -> Interactor:
    return Interactor(redis)
