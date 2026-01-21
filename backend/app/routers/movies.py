from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/movies", tags=["Movies"])
app = FastAPI(title="Movie Explorer API")

@router.get("/", response_model=list[schemas.Movie])
def get_movies(title: str = None, year: int = None, rating: float = None,
               director_id: int = None, genre_id: int = None, actor_id: int = None,
               db: Session = Depends(get_db)):
    filters = {k: v for k, v in locals().items() if v is not None and k != "db"}
    return crud.get_movies(db, filters)

@router.get("/{movie_id}", response_model=schemas.Movie)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.post("/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie)
