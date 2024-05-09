from pydantic import BaseModel

from src.models.base import BaseItem


class Hour(BaseModel):
    occupation: str
    room: BaseItem | None = None
