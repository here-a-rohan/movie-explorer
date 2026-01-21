# from sqlalchemy.orm import Session
# from app import models
# from app.database import engine, SessionLocal
#
# # 1️⃣ Create tables
# models.Base.metadata.create_all(bind=engine)
#
# db: Session = SessionLocal()
#
# # 2️⃣ Seed Genres
# genres = ["Action", "Adventure", "Sci-Fi", "Drama", "Comedy", "Thriller"]
# for g in genres:
#     db.add(models.Genre(name=g))
# db.commit()
#
# # 3️⃣ Seed Directors
# directors = ["Christopher Nolan", "Steven Spielberg", "Quentin Tarantino", "James Cameron", "Peter Jackson"]
# for d in directors:
#     db.add(models.Director(name=d))
# db.commit()
#
# # 4️⃣ Seed Actors
# actors = ["Leonardo DiCaprio", "Christian Bale", "Matthew McConaughey", "Tom Hanks",
#           "Samuel L. Jackson", "Brad Pitt", "Joseph Gordon-Levitt", "Anne Hathaway"]
# for a in actors:
#     db.add(models.Actor(name=a))
# db.commit()
#
# # 5️⃣ Seed Movies
# movies_data = [
#     {"title":"Inception","year":2010,"rating":8.8,"director_id":1,"genre_ids":[1,3],"actor_ids":[1,7,8]},
#     {"title":"The Dark Knight","year":2008,"rating":9.0,"director_id":1,"genre_ids":[1,6],"actor_ids":[2]},
#     {"title":"Interstellar","year":2014,"rating":8.6,"director_id":1,"genre_ids":[3,2],"actor_ids":[3,8]},
#     {"title":"Forrest Gump","year":1994,"rating":8.8,"director_id":2,"genre_ids":[4,5],"actor_ids":[4]},
#     {"title":"Pulp Fiction","year":1994,"rating":8.9,"director_id":3,"genre_ids":[1,6],"actor_ids":[5,6]},
#     {"title":"Titanic","year":1997,"rating":7.8,"director_id":4,"genre_ids":[4,2],"actor_ids":[1,8]},
#     {"title":"The Avengers","year":2012,"rating":8.0,"director_id":2,"genre_ids":[1,2],"actor_ids":[1,5]},
#     {"title":"The Lord of the Rings","year":2003,"rating":8.9,"director_id":5,"genre_ids":[2,4],"actor_ids":[6]},
# ]
#
# for m in movies_data:
#     movie = models.Movie(title=m["title"], year=m["year"], rating=m["rating"], director_id=m["director_id"])
#     movie.genres = [db.query(models.Genre).get(gid) for gid in m["genre_ids"]]
#     movie.actors = [db.query(models.Actor).get(aid) for aid in m["actor_ids"]]
#     db.add(movie)
#
# db.commit()
# db.close()
# print("Database seeded successfully!")
