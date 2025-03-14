from datetime import datetime
from uuid import uuid4
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import DateTime, String, func, Uuid, text, ForeignKey, Text, Integer


class Base(DeclarativeBase):
    id: Mapped[uuid4] = mapped_column(
        Uuid,
        primary_key=True,
        unique=True,
        default=uuid4,
        server_default=text("gen_random_uuid()"),
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        default=func.now(),
        server_default=func.now(),
        onupdate=func.now(),
    )


class User(Base):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)
    bookings: Mapped[list["Booking"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return (f"User(email={self.email!r}")


class Booking(Base):
    __tablename__ = "bookings"
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    user_id: Mapped[uuid4] = mapped_column(ForeignKey("users.id"))
    place_id: Mapped[uuid4] = mapped_column(ForeignKey("places.id"))
    user: Mapped["User"] = relationship(back_populates="bookings")
    place: Mapped["Place"] = relationship(back_populates="bookings")


class Place(Base):
    __tablename__ = "places"
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    bookings: Mapped[list["Booking"]] = relationship(back_populates="place")
