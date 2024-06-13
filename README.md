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
```

## Example Usage

To test the API, you can use tools like `curl`, Postman, or directly interact with the Swagger UI provided by FastAPI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Testing

### Running Tests with Pytest

Tests for the API were written using Pytest to ensure the endpoints work as expected. After writing the test cases, you can run the tests using the `pytest` command.

### Continuous Integration with GitHub Actions

A GitHub Actions workflow is set up to run the tests automatically on every push or pull request to the `main` branch. This ensures that the code is continuously tested and any issues are caught early.
