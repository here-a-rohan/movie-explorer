
# We dont have any post method so I have created on .py file to add the moviees directly
from app.database import SessionLocal
from app.models import Movie

db = SessionLocal()

movies = [
    Movie(title="Inception", year=2010, rating=8.8, genre="Sci-Fi"),
    Movie(title="The Dark Knight", year=2008, rating=9.0, genre="Action"),
    Movie(title="Interstellar", year=2014, rating=8.6, genre="Sci-Fi"),
    Movie(title="Forrest Gump", year=1994, rating=8.8, genre="Drama"),
]

db.add_all(movies)
print(db.query(Movie).all())
db.commit()
db.close()

print("Added!")
