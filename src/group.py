from pydantic import BaseModel, Field

from src.base import BaseItem
from src.hours import Hour


class Group(BaseModel):
    info: BaseItem = Field(alias="group")
    extramural: bool
    course: int
    number: int
    prefix: str
    hours: dict[int, dict[int, Hour]]
