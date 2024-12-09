# -- Pure Python Imports -- #
import typing
import inspect
# -- Backend Requirements Imports -- #
from fastapi import (
    FastAPI,
    APIRouter,
)
# -- Backend Package Imports -- #
from src.core import (
    get_settings,
    BackendSettings,
)
import src.api.controllers as all_controllers
from src.queue_stack import celery_app, add

settings: BackendSettings = get_settings()

# Get all the controllers from the controllers package, except for the "create_standard_controller" controller.
controllers: typing.List[APIRouter] = [
    controller
    for controller_name, controller in inspect.getmembers(all_controllers)
    if isinstance(controller, APIRouter) and controller_name != "create_standard_controller"
]

app = FastAPI(
    title="Example FASTAPI Backend",
    docs_url="/docs",
)

# Add all the controllers to the app.
for controller in controllers:
    app.include_router(controller)


@app.get("/")
def read_root():
    try:
        import redis
        r = redis.Redis(host='redis', port=6379, db=0)

        # Get the tasks from the queue
        print(r.lrange("default", 0, -1))
    except Exception as e:
        print(f"Connection failed: {e}")

    return {"Hello": "World"}


# Add the celery app to the app.
@app.post("/celery")
def launch_task():
    task_result = celery_app.send_task("add", args=[1, 2], queue="default")
    return {f"Task id: {task_result.id}"}


@app.get("/redis_queue")
def read_redis_queue():
    return {"queue": "read"}
