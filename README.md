# API Test Client

This project contains automated API tests for:

https://jsonplaceholder.typicode.com/posts

## Tech Stack

- Python
- pytest
- requests

## Project Structure

```text
api/
    posts_client.py

tests/
    test_posts_api.py
```

The API client layer is separated from the test cases to improve readability and maintainability.

## Setup Instructions

### Clone the repository

```bash
git clone <your-github-repository-url>
cd sdet-api-challenge
```

### Create virtual environment (optional)

```bash
python -m venv venv
```

Activate virtual environment:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest -v
```

## Test Coverage

- Get all posts
- Get single post
- Create post
- Update post
- Delete post
- Negative test for invalid post