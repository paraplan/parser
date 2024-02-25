from pydantic import BaseModel, Field, root_validator

from vgpk_parser import BaseItem
from vgpk_parser.schedule import Schedule


class SubGroupSchedules(BaseModel):
    lessons: list[Schedule]

    @root_validator(pre=True)  # refactor: should probably be changed to non-root validator
    def convert_dict_to_list(cls, values: dict):
        values["lessons"] = list(Schedule(**value) for value in values.values())
        return values


class GroupInfo(BaseModel):
    schedules: list[SubGroupSchedules] = Field(validation_alias="schedule")
    group: BaseItem

    @root_validator(pre=True)  # refactor: should probably be changed to non-root validator
    def convert_dict_to_list(cls, values):
        schedules = values.get("schedule", {})
        if isinstance(schedules, dict):
            values["schedule"] = [SubGroupSchedules(**item) for _, item in schedules.items()]
        return values
