from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/genres", tags=["Genres"])

@router.get("/", response_model=list[schemas.Genre])
def get_genres(name: str = None, db: Session = Depends(get_db)):
    filters = {k: v for k, v in locals().items() if v is not None and k != "db"}
    return crud.get_genres(db, filters)

@router.get("/{genre_id}", response_model=schemas.Genre)
def get_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = crud.get_genre(db, genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre

@router.post("/", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreBase, db: Session = Depends(get_db)):
    return crud.create_genre(db, genre)
