import redis.asyncio as aioredis  # type: ignore

from src.domain.protocols.inmemory import InMemoryProtocol


class RedisService(InMemoryProtocol):
    def __init__(self, redis: aioredis.Redis):
        self._redis = redis

    async def set_value(self, key: str, value: str) -> None:
        async with self._redis as r:
            await r.set(key, value)

    async def get_value(self, key: str) -> str:
        async with self._redis as r:
            return await r.get(key)
