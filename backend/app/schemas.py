from pydantic import BaseModel

class MovieSchema(BaseModel):
    id: int
    title: str
    year: int
    rating: float
    genre: str

    class Config:
        from_attributes = True
