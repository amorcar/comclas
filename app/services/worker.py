import os
import time

from celery import Celery


celery = Celery(
    __name__,
    broker=os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379"),
    backend=os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
)


@celery.task(name="create_task")
def create_task(text:str):
    time.sleep(10)
    return True
