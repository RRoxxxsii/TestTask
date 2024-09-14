from fastapi import FastAPI
import redis.asyncio as aioredis  # type: ignore

from src.presentation.api.di.adapters import AIORedisProvider, get_aioredis


def setup_providers(app: FastAPI, redis_pool: aioredis.Redis):
    redis = AIORedisProvider(redis_pool)
    app.dependency_overrides[get_aioredis] = redis.provide  # noqa
