from pydantic import BaseModel, EmailStr, Field, UUID4
from datetime import datetime


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str


class PlaceSchema(BaseModel):
    name: str = Field(max_length=100)
    description: str = Field(max_length=10000)
    capacity: int = Field(gt=0, lt=5000)


class BookingSchema(BaseModel):
    user_id: UUID4
    place_id: UUID4
    start_time: datetime = Field(datetime.now().isoformat())
    end_time: datetime = Field(datetime.now().isoformat())
