from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/directors", tags=["Directors"])

@router.get("/", response_model=list[schemas.Director])
def get_directors(name: str = None, movie_id: int = None, genre_id: int = None,
                  db: Session = Depends(get_db)):
    filters = {k: v for k, v in locals().items() if v is not None and k != "db"}
    return crud.get_directors(db, filters)

@router.get("/{director_id}", response_model=schemas.Director)
def get_director(director_id: int, db: Session = Depends(get_db)):
    director = crud.get_director(db, director_id)
    if not director:
        raise HTTPException(status_code=404, detail="Director not found")
    return director

@router.post("/", response_model=schemas.Director)
def create_director(director: schemas.DirectorBase, db: Session = Depends(get_db)):
    return crud.create_director(db, director)
