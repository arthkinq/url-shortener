# URL Shortener API

A simple URL shortener REST API service built with Python.

## How it works
The service takes a long URL from the user and generates a unique 6-character Base62 short ID. 
When a user navigates to the short URL, the service automatically redirects them to the original URL and increments a click counter. You can also view statistics for each shortened link, including its creation date and total clicks.

## Tech Stack
* **Framework:** FastAPI
* **Database:** SQLite + SQLAlchemy 2.0 (ORM)
* **Migrations:** Alembic
* **Validation & Serialization:** Pydantic V2
* **Testing:** pytest, httpx

## How to run the project

1. Clone the repository and navigate to the project directory:
   ```bash
   cd url-shortener
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```
   *(Note: The database tables will be created automatically on the first startup.)*

5. Open the interactive API documentation (Swagger UI) in your browser:
   http://127.0.0.1:8000/docs

## Running Tests

To run the unit tests (which use an isolated in-memory SQLite database), simply execute:
```bash
pytest
```
