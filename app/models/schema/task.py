from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel
from app.models.schema.base import BaseResponse


class Payload(BaseModel):
    '''
    Payload to classify
    '''
    text:str


class CreateTaskInfo(BaseModel):
    created: bool
    id: Optional[str] = None
    error: Optional[str] = None


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
    created_timestamp: Optional[datetime]
    status:str


class CreateTaskResponse(BaseResponse):
    '''
    Response to the create task action
    '''
    info: CreateTaskInfo

    class Config:
        schema_extra = {
            "example": {
                "info": {
                    "created": True,
                    "id": '0880f18f-3328-49a5-8bf9-707764079c57',
                    "error": None,
                }
            }
        }


class TaskStatusResponse(BaseResponse):
    '''
    Response to the check task status action
    Possible status:
        PENDING
        STARTED
        SUCCESS
        FAILURE
        PROGRESS
        RETRY
        REVOKED
        ERROR
    '''
    task_status: Optional[TaskStatus]
    result: Optional[TaskResult] = None
    error: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "task_status": {
                    "id": '0880f18f-3328-49a5-8bf9-707764079c57',
                    "created_timestamp": '2022-03-26T17:54:57.682684+00:00',
                    "status": "PROGRESS",
                },
                "result": {
                    "value": None,
                },
                "error": None,
            }
        }
