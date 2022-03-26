from pydantic import BaseModel
from app.models.schema.base import BaseResponse

class Distance(BaseModel):
    meters: float

class DistanceResponse(BaseResponse):
    meters: float
