from pydantic import BaseModel, Field

from src.models.base import BaseItem
from src.models.group import Group


class Area(BaseModel):
    info: BaseItem = Field(validation_alias="area")
    color: str
    groups: list[Group]
