from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import engine, Base, get_db
from fastapi.middleware.cors import CORSMiddleware
from app.routers import movies, actors, directors, genres
from fastapi import HTTPException
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Explorer API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Movie routers
@app.get("/movies", response_model=list[schemas.Movie])
def read_movies(
    title: str | None = None,
    year: int | None = None,
    rating: float | None = None,
    director: str | None = None,
    genre: str | None = None,
    actor: str | None = None,
    db: Session = Depends(get_db)
):
    filters = {
        k: v for k, v in {
            "title": title,
            "year": year,
            "rating": rating,
            "director": director,
            "genre": genre,
            "actor": actor,
        }.items() if v is not None
    }

    return crud.get_movies(db, filters)

@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie_by_id(db, movie_id)

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    return movie


