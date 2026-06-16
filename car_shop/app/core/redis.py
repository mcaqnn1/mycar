from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache import FastAPICache
from redis import asyncio as aioredis
from contextlib import asynccontextmanager
from fastapi import FastAPI
from .settings import get_settings
import logging

logger = logging.getLogger(__name__)
settings = get_settings()

@asynccontextmanager
async def lifespan(app:FastAPI):
    redis = aioredis.from_url(
        settings.REDIS_URL,
        encoding="utf-8",
        decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis=redis))
    logger.info("Connected!")
    yield 
    await redis.close()
    logger.info("Disconnected!")



