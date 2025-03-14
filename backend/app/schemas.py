from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class BaseModelWithORM(BaseModel):
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class User(BaseModelWithORM):
    id: int
    email: EmailStr


class Place(BaseModelWithORM):
    id: int
    name: str = Field(max_length=100)
    description: str = Field(max_length=10000)
    capacity: int = Field(gt=0, lt=5000)


class BookingCreate(BaseModel):
    place_id: int
    start_time: datetime = Field(datetime)
    end_time: datetime = Field(datetime)


class Booking(BaseModelWithORM):
    id: int
    user_id: int
    place_id: int
    start_time: datetime = Field(datetime)
    end_time: datetime = Field(datetime)
