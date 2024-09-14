import redis.asyncio as aioredis  # type: ignore


def build_redis(url: str) -> aioredis.Redis:
    redis = aioredis.from_url(
        url,
        encoding="utf-8",
        decode_responses=True,
    )
    return redis
