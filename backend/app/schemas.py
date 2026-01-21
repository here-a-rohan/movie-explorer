from typing import List
from pydantic import BaseModel

class GenreBase(BaseModel):
    name: str

class Genre(GenreBase):
    id: int
    model_config = {
        "from_attributes": True
    }

class DirectorBase(BaseModel):
    name: str

class Director(DirectorBase):
    id: int
    model_config = {
        "from_attributes": True
    }

class ActorBase(BaseModel):
    name: str

class Actor(ActorBase):
    id: int
    model_config = {
        "from_attributes": True
    }

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
    model_config = {
        "from_attributes": True
    }
