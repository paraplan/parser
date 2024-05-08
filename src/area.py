from pydantic import BaseModel, Field

from src.base import BaseItem
from src.group import Group


class Area(BaseModel):
    info: BaseItem = Field(alias="area")
    color: str
    groups: list[Group]
