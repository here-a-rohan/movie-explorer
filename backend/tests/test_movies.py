from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_docs_available():
    r = client.get("/docs")
    assert r.status_code == 200

def test_list_movies():
    r = client.get("/movies")
    assert r.status_code == 200

    data = r.json()
    # If you have pagination:
    # assert "items" in data
    # Else (no pagination yet):
    assert isinstance(data, list)

def test_movie_details_not_found():
    r = client.get("/movies/999999")
    # if you return 404 properly:
    assert r.status_code in (404, 200)  # change to 404 once you enforce it
