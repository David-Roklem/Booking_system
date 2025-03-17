from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.UserCreateSchema)
def create_user(user: schemas.UserCreateSchema, db: Session = Depends(get_db)):
    crud.create_user(db=db, user=user)
    return user


@app.get("/places/", response_model=list[schemas.PlaceSchema])
def read_places(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    places = crud.get_places(db, skip=skip, limit=limit)
    return places


@app.post("/bookings/", response_model=schemas.BookingSchema)
def create_booking(booking: schemas.BookingSchema, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, booking=booking, user_id=1)  # Замените на реальный user_id
