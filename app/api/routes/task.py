# from fastapi import APIRouter, Body, Depends, HTTPException
# from starlette.status import HTTP_400_BAD_REQUEST
from fastapi import APIRouter, Body

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
    name="Post a Text to a new classifier task")
async def api_create_task(
        payload: Payload
) -> CreateTaskResponse:
    payload = payload.dict()
    return CreateTaskResponse(**(await create_task(payload)))

@router.get(
    "/{task_id}",
    status_code=200,
    response_model=TaskStatusResponse,
    name="Check a certain classifier task status")
async def api_check_task_status(
        task_id: int,
) -> TaskStatusResponse:
    return TaskStatusResponse(**(await get_task_status(task_id=task_id)))
