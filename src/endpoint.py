from datetime import date

import orjson
from fastapi import APIRouter

from src.fetch import get_raw_schedule
from src.models.study_day import StudyDay

router = APIRouter()


@router.get("/study_day", response_model=StudyDay)
async def get_study_day(date: date):
    raw_schedule = await get_raw_schedule(date)
    return orjson.loads(raw_schedule)


@router.get("/raw_study_day")
async def get_raw_study_day(date: date) -> bytes:
    return await get_raw_schedule(date)
