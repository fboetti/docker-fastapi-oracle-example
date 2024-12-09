from celery import Celery
from src.core.database_connection import get_database_url_from_settings
from src.queue_stack.celery import CelerySettings

__all__ = [
    "celery_app",
    "add",
]


celery_app: Celery = Celery(
    "celery_worker",
    backend=f"db+{get_database_url_from_settings()}",
    **CelerySettings().dict(),
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="Europe/Rome",
)


@celery_app.task
def add(x, y):
    print(f"Adding {x} + {y}")
    return x + y
