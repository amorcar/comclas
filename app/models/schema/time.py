from datetime import datetime
from app.models.schema.base import BaseResponse


class UTCTime(BaseResponse):
    utc_timestamp: float


class FormattedUTCTime(BaseResponse):
    utc_timestamp: str

    @classmethod
    def from_timestamp(cls, timestamp: float):
        return cls(utc_timestamp=str(datetime.fromtimestamp(timestamp)))
