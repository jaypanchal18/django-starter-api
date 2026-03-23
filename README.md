# Django Starter API

## Project Structure

This is a starter template for a Django REST API project using PostgreSQL as the database.

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- PostgreSQL
- Docker
- pytest

### Installation

1. Clone the repository
2. Navigate to the project directory
3. Run `docker-compose up` to start the services

### Directory Structure

django_starter_api/
│
├── app/
│   ├── manage.py
│   ├── django_starter_api/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── api/
│       ├── __init__.py
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       └── urls.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
└── tests/
    ├── __init__.py
    └── test_api.py
### Getting Started

1. **Create a virtual environment** (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   2. **Install dependencies**:
   pip install django djangorestframework psycopg2
   3. **Set up PostgreSQL**:
   - Ensure PostgreSQL is running and create a database for the project.

4. **Configure settings.py**:
   - Update the DATABASES setting with your PostgreSQL credentials.

5. **Run migrations**:
   python manage.py migrate
   6. **Run the server**:
   python manage.py runserver
   ### Running Tests

To run the tests, use:
pytest tests/
### License

This project is licensed under the MIT License - see the LICENSE file for details.