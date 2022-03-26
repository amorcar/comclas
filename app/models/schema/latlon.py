from pydantic.main import BaseModel
from app.models.schema.base import BaseResponse

class LatLonDecimal(BaseModel):
    '''
    A latitude, longitude GPS point in decimal notation.
    '''
    latitude: float
    longitude: float

    class Config:
        schema_extra = {
            "example": {
                "latitude": 40.41694,
                "longitude": -3.70361,
            }
        }

class LatLonDMS(BaseModel):
    '''
    A latitude, longitude GPS point in degrees, minutes and seconds notation.
    Coordinates are represented as strings with the format XX°XX′X.XX″ N/S/W/E
    '''
    latitude: float
    longitude: float

    class Config:
        schema_extra = {
            "example": {
                "latitude": "40°25′0.98″ N",
                "longitude": " 3°42′13″ W",
            }
        }

class LatLonDecimalResponse(BaseResponse):
    coordinates: LatLonDecimal

class LatLonDMSResponse(BaseResponse):
    coordinates: LatLonDMS
