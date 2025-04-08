# filepath: app/infra/celery.py
import os
from celery import Celery

celery_app = Celery(
    "tasks",
    broker=os.getenv("REDIS_URL"),
    backend=os.getenv("REDIS_URL"),
)