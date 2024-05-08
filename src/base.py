from pydantic import BaseModel, Field


class BaseItem(BaseModel):
    full_name: str = Field(alias="fullname")
    name: str
    id: int = Field(alias="value")
