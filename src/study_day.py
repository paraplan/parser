from datetime import date
from pydantic import BaseModel

from src.area import Area
from src.bells import Bells


class StudyDay(BaseModel):
    date: date
    bells: Bells
    areas: list[Area]
