from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str


class PlaceSchema(BaseModel):
    name: str = Field(max_length=100)
    description: str = Field(max_length=10000)
    capacity: int = Field(gt=0, lt=5000)


class BookingSchema(BaseModel):
    user_id: int
    place_id: int
    start_time: datetime = Field(datetime)
    end_time: datetime = Field(datetime)
