from pydantic import BaseModel, Field

from src.models.base import BaseItem
from src.models.hours import Hour


class Group(BaseModel):
    """
    Class for groups

    The Hours field should be a list or dict in random order (I dont know why).
    """

    info: BaseItem = Field(validation_alias="group")
    extramural: bool
    course: int
    number: int
    prefix: str
    hours: dict[int, dict[int, Hour]] | list[dict[int, Hour]]
