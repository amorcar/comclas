from datetime import datetime
from pydantic import BaseModel
from app.core.config import VERSION


class BaseResponse(BaseModel):
    version: str = VERSION
    server_time: datetime
