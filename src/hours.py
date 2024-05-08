from pydantic import BaseModel

from src.base import BaseItem


class Hour(BaseModel):
    occupation: str
    room: BaseItem | None = None
