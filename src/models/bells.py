from datetime import time

from pydantic import BaseModel

from src.models.base import BaseItem


class BellsHours(BaseModel):
    start: time
    end: time


class Bells(BaseModel):
    name: str
    id: BaseItem
    hours: list[BellsHours]
