# AdminOS-Lab

A digital cupboard for lab offices.

## Setup

1.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up environment variables:**
    Copy the `.env.example` file to `.env`. A default `SECRET_KEY` is provided.
    ```bash
    cp .env.example .env
    ```

## Running the Application

1.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

2.  **Seed the database with sample data:**
    ```bash
    python manage.py seed_data
    ```

3.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

## Running Tests

To run the test suite, use `pytest`:
```bash
pytest
```

## Endpoints

- `/health/`: Returns a JSON response with the status of the application.