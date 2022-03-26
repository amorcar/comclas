# from app.services.worker import create_celery_task

async def create_task(payload:dict) -> dict:
    text = payload['text']
    # task = create_celery_task.delay(text)
    return {
        'created': True,
        'id': len(text),
        # 'id': task.id,
        'error': None,
    }

async def get_task_status(task_id: int) -> dict:
    return {
            'status': 'RUNNING',
            'id': task_id,
            'return_value': None,
            'error': None,
    }
