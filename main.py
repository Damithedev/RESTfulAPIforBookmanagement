import uuid
from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, UUID1, validator, ValidationError, UUID3
from random import randint
from datetime import datetime

app = FastAPI()

books = []


class Book(BaseModel):
    #id will be assigned after Object is created
    id: Optional[int] = None
    title: str
    author: str
    published_year: int

    #validate Published year if it is Valid
    @validator('published_year')
    def published_year_must_be_valid(cls, value):
        if value < 1500:
            raise ValueError("Published year must be above 1500")
        if value > datetime.now().year:
            raise ValueError("Published year must be before today")
        return value


@app.get('/')
async def home():
    return {"Welcome to BOOKS by D"}


@app.get('/books')
async def get_books():
    book_list = [book["title"] for book in books]
    return book_list


@app.post('/addbooks', status_code=status.HTTP_201_CREATED)
async def add_new_book(book: Book):
    #book id is given the index of Book object in books
    book.id = len(books)
    books.append(book.dict())

    print(books)
    return {"message": f"Book by {book.author} added successfully"}


@app.get('/books/{id}')
async def get_book(id: int):

    if id < len(books):
        return books[id]
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@app.put('/books/{id}')
async def update_book(id: int, book: Book):
    if id < len(books):
        books[id] = book.dict()
        return {"message": f"This book by {book.author} updated"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")


@app.delete('/books/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int):
    if id < len(books):
        books.pop(id)
        return {"message": f"This book with id:{id} deleted"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")
