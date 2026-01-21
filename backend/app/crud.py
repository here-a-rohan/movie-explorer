from sqlalchemy.orm import Session
from . import models
from fastapi import HTTPException



# Movies
def get_movies(db: Session, filters: dict = {}):
    query = db.query(models.Movie)

    if filters.get("title"):
        query = query.filter(models.Movie.title.ilike(f"%{filters['title']}%"))

    if filters.get("year"):
        query = query.filter(models.Movie.year == filters["year"])

    if filters.get("rating"):
        query = query.filter(models.Movie.rating >= filters["rating"])

    if filters.get("director"):
        query = query.join(models.Movie.director).filter(
            models.Director.name.ilike(f"%{filters['director']}%")
        )

    if filters.get("genre"):
        query = query.join(models.Movie.genres).filter(
            models.Genre.name.ilike(f"%{filters['genre']}%")
        )

    if filters.get("actor"):
        query = query.join(models.Movie.actors).filter(
            models.Actor.name.ilike(f"%{filters['actor']}%")
        )

    return query.distinct().all()

def get_movie_by_id(db: Session, movie_id: int):
    return (
        db.query(models.Movie)
        .filter(models.Movie.id == movie_id)
        .first()
    )
