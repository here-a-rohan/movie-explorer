from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/actors", tags=["Actors"])

@router.get("/", response_model=list[schemas.Actor])
def get_actors(name: str = None, movie_id: int = None, genre_id: int = None,
               db: Session = Depends(get_db)):
    filters = {k: v for k, v in locals().items() if v is not None and k != "db"}
    return crud.get_actors(db, filters)

@router.get("/{actor_id}", response_model=schemas.Actor)
def get_actor(actor_id: int, db: Session = Depends(get_db)):
    actor = crud.get_actor(db, actor_id)
    if not actor:
        raise HTTPException(status_code=404, detail="Actor not found")
    return actor

@router.post("/", response_model=schemas.Actor)
def create_actor(actor: schemas.ActorBase, db: Session = Depends(get_db)):
    return crud.create_actor(db, actor)
