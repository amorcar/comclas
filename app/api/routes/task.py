# from fastapi import APIRouter, Body, Depends, HTTPException
# from starlette.status import HTTP_400_BAD_REQUEST
from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse

# from app.services.worker import create_task


router = APIRouter()

@router.post(
    "/",
    status_code=201,
    # response_model=,
    name="Post a Text to a new classifier task")
async def run_task(
        payload = Body(...),
) -> JSONResponse:
    print(payload)
    text = payload['text']
    # task = create_task.delay(text)
    # return JSONResponse({'task_id': task.id})
    return JSONResponse({'task_id': len(text)})

@router.get(
    "/{task_id}",
    # status_code=201,
    # response_model=,
    name="Check a certain classifier task status")
async def get_task_status(
        task_id: int,
) -> JSONResponse:
    return JSONResponse(task_id)
