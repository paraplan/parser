from datetime import date

from pydantic import BaseModel

from src.models.area import Area
from src.models.bells import Bells


class StudyDay(BaseModel):
    date: date
    bells: Bells
    areas: list[Area]
