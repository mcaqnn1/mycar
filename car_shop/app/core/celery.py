from celery import Celery
from database.config import get_settings

settings = get_settings()

celery = Celery(
    backend=settings.REDIS_URL,
    broker=settings.REDIS_URL,
    include=["tasks.task"]
)

