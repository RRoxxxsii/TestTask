from collections.abc import AsyncGenerator

import redis.asyncio as aioredis  # type: ignore

from src.infrastructure.redis.service import RedisService


def get_aioredis():
    pass


class AIORedisProvider:
    def __init__(self, redis: aioredis.Redis):
        self.redis = redis

    async def provide(self) -> AsyncGenerator[aioredis.Redis, None]:
        async with self.redis.client() as client:
            yield RedisService(client)
