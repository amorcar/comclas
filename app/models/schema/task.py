from typing import Optional, Any
from pydantic import BaseModel
from app.models.schema.base import BaseResponse

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
    status: str
    id: int
    return_value: Optional[Any] = None
    error: Optional[bool] = None

    class Config:
        schema_extra = {
            "example": {
                "status": "RUNNING",
                "id": 0,
                "return_value": None,
                "error": None,
            }
        }
