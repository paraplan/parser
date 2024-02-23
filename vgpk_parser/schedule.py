from pydantic import BaseModel, Field

from vgpk_parser import BaseItem


class Schedule(BaseModel):
    lecturer: BaseItem | None
    room: BaseItem | None
    type: int
    occupation: BaseItem
    title: str = Field(validation_alias="occname")
