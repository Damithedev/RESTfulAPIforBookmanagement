from fastapi.testclient import TestClient
from main import app,books

client = TestClient(app)
books.clear()
def test_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ['Welcome to BOOKS by D']

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert response.json() == []

def test_add_book():
    response = client.post("/addbooks", json={"title": "Cook Rednbeans", "author": "Dami", "published_year": 2000})
    assert response.status_code == 201
    assert response.json() == {"message": f"Book by Dami added successfully"}

def test_update_book():
    client.post("/addbooks", json={"title": "Cook Rednbeans", "author": "Dami", "published_year": 2000})
    response = client.put("/books/0", json={"title": "Cook Yellow Bean", "author": "Dami", "published_year": 2000})
    assert response.status_code == 200
    assert response.json() == {"message": "This book by Dami updated"}


def test_delete_book():
    client.post("/addbooks", json={"title": "Cook Rednbeans", "author": "Dami", "published_year": 2000})
    response = client.delete("/books/0")
    assert response.status_code == 204


