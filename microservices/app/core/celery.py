from celery import Celery
from core.settings import settings

celery = Celery(
    "tasks",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=["tasks.task"]
)