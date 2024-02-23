from datetime import date

from pydantic import BaseModel

from vgpk_parser import BaseItem
from vgpk_parser.group import GroupInfo


class StudyDay(BaseModel):
    date: date
    groups: list[GroupInfo]
    bells: BaseItem
