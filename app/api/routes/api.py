from typing import Optional, Union
from fastapi import APIRouter
from fastapi.params import Query
from starlette.responses import RedirectResponse

from app.models.schema.time import UTCTime, FormattedUTCTime
from app.services.timestamps import get_current_UTC
from app.api.routes import task

router = APIRouter()


@router.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")


@router.get(
    "/utc/",
    response_model=Union[UTCTime, FormattedUTCTime],
    name="Get current UTC timestamps",
    tags=["timestamp"],
)
def get_utc_timestamp(strf: Optional[bool] = Query(False)):
    if strf:
        return FormattedUTCTime.from_timestamp(get_current_UTC())
    return UTCTime(utc_timestamp=get_current_UTC())


router.include_router(task.router, tags=["text classification"], prefix="/task")
