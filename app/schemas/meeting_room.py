# app/schemas/meeting_room.py

from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomCreate(BaseModel):
    name: str  = Field(
        ..., max_length=100)
    description: Optional[str]

    @validator('name')
    def name_cant_be_empty(cls, value: str):
        if not value:
            raise ValueError('Имя обязательно к заполнению')
        return value