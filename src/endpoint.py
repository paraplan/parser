from datetime import date

import orjson
from fastapi import APIRouter
from pydantic import BaseModel

from src.fetch import get_schedule
from src.study_day import StudyDay

router = APIRouter()


class APIError(BaseModel):
    code: int
    message: str


@router.get("/study_day", response_model=StudyDay)
async def get_study_day(date: date):
    schedule = await get_schedule(date)
    return orjson.loads(schedule)


@router.get("/raw_study_day")
async def get_raw_study_day(date: date) -> bytes:
    return await get_schedule(date)
