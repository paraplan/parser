from pydantic import BaseModel, Field, RootModel

from vgpk_parser import BaseItem
from vgpk_parser.schedule import Schedule


class SubGroupSchedules(RootModel):
    root: dict[int, Schedule]


class GroupSchedules(RootModel):
    root: dict[int, SubGroupSchedules]


class GroupInfo(BaseModel):
    schedules: GroupSchedules = Field(validation_alias="schedule")
    group: BaseItem
