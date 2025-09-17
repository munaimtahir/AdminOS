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

## Run in development (dev settings)
```bash
# activate venv first
export DJANGO_SETTINGS_MODULE=adminos_lab.dev_settings
python manage.py migrate
python manage.py runserver 0.0.0.0:8001
```

In production, use the default:

```bash
# DJANGO_SETTINGS_MODULE defaults to adminos_lab.settings
# DEBUG should be 0 and ALLOWED_HOSTS set to your domain/IP in .env
```

## Running Tests

To run the test suite, use `pytest`:
```bash
pytest
```

## Application Pages

The following pages are available:

-   **/ (Dashboard)
    -   Shows the status of all register pages for the current day.
-   **/registers/
    -   Lists all available registers and provides a link to the current day's page for each.
-   **/bundles/daily/
    -   A bundle view showing all register pages for the current day.
-   **/bundles/weekly/
    -   A bundle view showing all register pages for the current week (Monday to Sunday).
-   **/bundles/pending/
    -   A bundle view showing all register pages that are overdue or due today.
-   **/admin/
    -   The Django admin interface for managing all data models.
-   **/health/
    -   A health check endpoint that returns a JSON response with the status of the application.