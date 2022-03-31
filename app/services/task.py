from datetime import datetime
from app.services.worker import create_celery_task
from celery.result import AsyncResult


async def create_task(payload: dict) -> dict:
    text = payload["text"]
    try:
        task = create_celery_task.delay(text)
        return {
            "server_time": datetime.utcnow().timestamp(),
            "info": {
                "created": True,
                "id": task.id,
                "error": None,
            },
        }
    except Exception as e:
        return {
            "server_time": datetime.utcnow().timestamp(),
            "info": {
                "created": False,
                "id": None,
                "error": str(e),
            },
        }


async def get_task_status(task_id: str) -> dict:
    task_result = AsyncResult(task_id)
    task_status = task_result.status
    # TODO: check if task_id exist & return error if it doesn't
    if task_status == "PENDING":
        return {
            "server_time": datetime.utcnow().timestamp(),
            "task_status": {
                "id": task_id,
                "created_timestamp": None,
                "status": "ERROR",
            },
            "result": {
                "value": None,
            },
            "error": "Task ID not found",
        }
    task_return_value = task_result.info.get("result", None)
    created_at = task_result.info.get("created_at", None)
    error = task_result.info.get("error", None)
    return {
        "server_time": datetime.utcnow().timestamp(),
        "task_status": {
            "id": task_id,
            "created_timestamp": created_at,
            "status": task_status,
        },
        "result": {
            "value": task_return_value,
        },
        "error": error,
    }
