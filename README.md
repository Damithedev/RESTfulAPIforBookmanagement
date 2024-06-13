# Book Management API

This is a simple Book Management API built with FastAPI that allows you to perform CRUD operations on a collection of books.

## Features

- Add a new book to the collection.
- Retrieve the list of books.
- Retrieve details of a specific book by ID.
- Update details of a specific book by ID.
- Delete a specific book by ID.

## Requirements

- Python 3.7+
- FastAPI
- Pydantic

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the API

Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
