from pydantic import BaseModel


class FallbackBells(BaseModel):
    Zero: list[str]
    First: list[str]
    Second: list[str]
    Third: list[str]
    Fourth: list[str]
    Fifth: list[str]


class FallbackSchedule(BaseModel):
    _id: int
    bells: list[FallbackBells]
