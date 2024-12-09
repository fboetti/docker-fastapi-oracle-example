from typing import Optional
from pydantic_settings import BaseSettings

__all__ = [
    "CelerySettings",
]


class CelerySettings(BaseSettings):
    """
        Base settings for the celery app instance, every setting can be overridden by
        environment variable prefixed by CELERY_
        for example to enable aks_late: CELERY_AKS_LATE=true
    """

    # Worker name used to identify the worker.
    worker_name: str = "celery_worker"
    # Broker URL, specifies the message broker to use.
    broker: str = "redis://redis:6379"
    # Default queue name.
    task_default_queue: str = "default"

    task_default_exchange: str = "default"
    task_default_exchange_type: str = "direct"
    task_default_routing_key: str = "default"
    task_queues: Optional[tuple] = None
    autodiscover_tasks: list = [""]
    task_routes: dict = {}
    task_track_started: bool = True
    task_acks_late: bool = False
    # with true we can send tasks to queues that do not exist
    # so are defined in other codebases
    task_create_missing_queues: bool = True
    worker_concurrency: int = 1
    worker_prefetch_multiplier: int = 1
    result_extended: bool = True

    class Config:
        env_prefix = "CELERY_"
