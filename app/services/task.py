from app.services.worker import create_celery_task
from celery.result import AsyncResult

async def create_task(payload:dict) -> dict:
    text = payload['text']
    task = create_celery_task.delay(text)
    return {
        'created': True,
        # 'id': len(text),
        'id': task.id,
        'error': None,
    }

async def get_task_status(task_id: str) -> dict:
    task_result = AsyncResult(task_id)
    task_status = task_result.status
    task_return_value = task_result.result
    return {
            'status': task_status,
            'id': task_id,
            'return_value': task_return_value,
            'error': None,
    }
