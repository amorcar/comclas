from typing import Optional, Any
from pydantic import BaseModel
from app.models.schema.base import BaseResponse


class Payload(BaseModel):
    '''
    Payload to classify
    '''
    text:str


class TaskResult(BaseModel):
    '''
    Task Result object
    '''
    value: Optional[Any]

class TaskStatus(BaseModel):
    '''
    Task Status object
    '''
    id:str
    status:str


class CreateTaskResponse(BaseResponse):
    '''
    Response to the create task action
    '''
    created: bool
    id: Optional[str] = None
    error: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "created": True,
                "id": '0880f18f-3328-49a5-8bf9-707764079c57',
                "error": None,
            }
        }


class TaskStatusResponse(BaseResponse):
    '''
    Response to the check task status action
    Possible status:
        PENDING
        SUCCESS
        ERROR
    '''
    created_timestamp: Optional[int]
    task_status: Optional[TaskStatus]
    result: Optional[TaskResult] = None
    error: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "status": {
                    "id": '0880f18f-3328-49a5-8bf9-707764079c57',
                    "status": "PENDING",
                },
                "result": {
                    "value": None,
                },
                "error": None,
            }
        }
