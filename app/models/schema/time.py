from datetime import datetime
from pydantic import BaseModel


class UTCTime(BaseModel):
    utc_timestamp: float


class FormattedUTCTime(BaseModel):
    utc_timestamp: str

    @classmethod
    def from_timestamp(cls, timestamp: float):
        return cls(utc_timestamp=str(datetime.fromtimestamp(timestamp)))
