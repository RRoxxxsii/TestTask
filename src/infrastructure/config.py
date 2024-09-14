from dataclasses import dataclass

from src.infrastructure.redis.config import RedisConfig


@dataclass(frozen=True)
class Config:
    redis: RedisConfig = RedisConfig()


def get_config() -> Config:
    return Config()
