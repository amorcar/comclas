from pydantic import BaseModel
from app.core.config import VERSION

class BaseResponse(BaseModel):
    version: str = VERSION