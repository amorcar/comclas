from typing import Optional, Any
from pydantic import BaseModel
from app.models.schema.base import BaseResponse


class Payload(BaseModel):
    '''
    Payload to classify
    '''
    text:str


class Task(BaseModel):
    '''
    Task object
    '''
    id:int
    status:str
    created_timestamp:int
    payload:Payload
    return_value: Optional[Any]


class CreateTaskResponse(BaseResponse):
    '''
    Response to the create task action
    '''
    created: bool
    id: Optional[int] = None
    error: Optional[bool] = None

    class Config:
        schema_extra = {
            "example": {
                "created": True,
                "id": 0,
                "error": None,
            }
        }


class TaskStatusResponse(BaseResponse):
    '''
    Response to the check task status action
    Possible status:
        RUNNING
        QUEUED
        STOPPED
        FINNISHED
        ERROR
    '''
    id: int
    status: str
    return_value: Optional[Any] = None
    error: Optional[bool] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 0,
                "status": "RUNNING",
                "return_value": None,
                "error": None,
            }
        }
