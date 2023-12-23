# Django Multi-Tenant Application

This project is a multi-tenant Django application that implements a REST API for managing findings with multi-database server support. It includes APIs for adding and retrieving findings per tenant, with support for distributing tenants across different database servers.

## Installation

### Prerequisites

- Python 3.9 or later
- Docker and Docker Compose (optional)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/multi-tenant-application.git
    cd multi-tenant-application
    ```

2. Create a virtual environment (recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # For Linux/macOS
    # or
    .\env\Scripts\activate  # For Windows
    ```

3. Install dependencies using Poetry:

    ```bash
    poetry install
    ```

4. Set up Django environment variables:

    - Copy `settings_local.example.py` to `settings_local.py`.
    - Update `settings_local.py` with your environment-specific settings.

5. Run Migrations:

    ```bash
    python manage.py migrate
    ```

## Running the Project

### Option 1: Using Docker (recommended)

1. Ensure Docker is installed and running.
2. Run the following command:

    ```bash
    docker-compose up
    ```

### Option 2: Without Docker

1. Run the Django server:

    ```bash
    python manage.py runserver
    ```

## Accessing the Application

Once the server is running:

- Access the Swagger at `http://localhost:8000/api/v1/swagger/`.
- Use the REST APIs for managing findings (e.g., `http://localhost:8000/api/v1/findings/`).

## Running Tests

To run tests with pytest:

```bash
poetry run pytest
```
