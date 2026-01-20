from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import Movie

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/movies")
def list_movies(genre: str | None = None, db: Session = Depends(get_db)):
    """
    Return all movies.
    Filtering is handled on the backend using query params.
    """
    print('Rohan')
    query = db.query(Movie)
    if genre:
        query = query.filter(Movie.genre == genre)
    return query.all()
