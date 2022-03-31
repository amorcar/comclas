# from fastapi import APIRouter, Body, Depends, HTTPException
# from starlette.status import HTTP_400_BAD_REQUEST
from fastapi import APIRouter, Body, HTTPException

from app.models.schema.task import (
    Payload,
    CreateTaskResponse,
    TaskStatusResponse,
)
from app.services.task import (
    create_task,
    get_task_status,
)


router = APIRouter()


@router.post(
    "/",
    status_code=201,
    response_model=CreateTaskResponse,
    name="Post a Text to a new classifier task",
)
async def api_create_task(payload: Payload) -> CreateTaskResponse:
    payload = payload.dict()
    response = CreateTaskResponse(**(await create_task(payload)))

    if response.info.created:
        return response
    else:
        raise HTTPException(status_code=500, detail=response.error)


@router.get(
    "/{task_id}",
    status_code=200,
    response_model=TaskStatusResponse,
    name="Check a certain classifier task status",
)
async def api_check_task_status(
    task_id: str,
) -> TaskStatusResponse:
    return TaskStatusResponse(**(await get_task_status(task_id=task_id)))
