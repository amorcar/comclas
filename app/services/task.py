from app.services.worker import create_celery_task
from celery.result import AsyncResult

async def create_task(payload:dict) -> dict:
    text = payload['text']
    try:
        task = create_celery_task.delay(text)
        return {
            'created': True,
            'id': task.id,
            'error': None,
        }
    except Exception as e:
        return {
            'created': False,
            'id': None,
            'error': str(e),
        }


async def get_task_status(task_id: str) -> dict:
    task_result = AsyncResult(task_id)
    task_status = task_result.status
    task_return_value = task_result.result
    return {
            'created_timestamp': 0,
            'task_status': {
                'id': task_id,
                'status': task_status
            },
            'result': {
                'value': task_return_value,
            },
            'error': None,
    }
