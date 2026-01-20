from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Movie

app = FastAPI()

# --- CORS ---
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Movies endpoint ---
@app.get("/movies")
def list_movies(
    title: str | None = Query(None),
    year: int | None = Query(None),
    rating: float | None = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Movie)
    if title:
        query = query.filter(Movie.title.ilike(f"%{title}%"))
    if year:
        query = query.filter(Movie.year == year)
    if rating:
        query = query.filter(Movie.rating >= rating)

    movies = query.all()
    return movies
