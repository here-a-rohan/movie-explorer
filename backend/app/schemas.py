from typing import List
from pydantic import BaseModel

class GenreBase(BaseModel):
    name: str

class Genre(GenreBase):
    id: int
    class Config:
        orm_mode = True

class DirectorBase(BaseModel):
    name: str

class Director(DirectorBase):
    id: int
    class Config:
        orm_mode = True

class ActorBase(BaseModel):
    name: str

class Actor(ActorBase):
    id: int
    class Config:
        orm_mode = True

class MovieBase(BaseModel):
    title: str
    year: int
    rating: float
    director_id: int
    genre_ids: List[int] = []
    actor_ids: List[int] = []

class Movie(MovieBase):
    id: int
    director: Director
    genres: List[Genre] = []
    actors: List[Actor] = []
    class Config:
        orm_mode = True
