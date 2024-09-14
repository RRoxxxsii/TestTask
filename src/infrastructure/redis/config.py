import os
from dataclasses import dataclass


@dataclass(frozen=True)
class RedisConfig:
    url = os.getenv("REDIS_HOST")
