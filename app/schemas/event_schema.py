from datetime import datetime
from typing import Optional

from pydantic import BaseModel, model_validator


class EventBaseSchema(BaseModel):
    title: str
    description: str
    location: str
    date: datetime


class EventSchema(EventBaseSchema):
    id: int

    class Config:
        from_attributes = True


class EventCreateRequestSchema(EventBaseSchema):
    class Config:
        extra = "forbid"


class EventUpdateRequestSchema(EventBaseSchema):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    date: Optional[datetime] = None

    class Config:
        extra = "forbid"

    @model_validator(mode="before")
    def check_at_least_one_field(cls, values):
        if not any(values.values()):
            raise ValueError("At least one field must be provided to update the event")
        return values


class RegisterEventResponseSchema(BaseModel):
    registration_id: int
