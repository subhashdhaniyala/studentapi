# Student API

A production-ready REST API built with Django REST Framework.

## Features
- Full CRUD operations
- JWT Authentication
- Pagination (5 per page)
- Filtering by course and status
- Search by name and email
- Ordering by name and enrollment date

## Tech Stack
- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite

## API Endpoints
| Method | URL | Description |
|--------|-----|-------------|
| POST | /api/token/ | Get JWT token |
| POST | /api/token/refresh/ | Refresh token |
| GET | /api/student/ | List all students |
| POST | /api/student/ | Create student |
| GET | /api/student/1/ | Get one student |
| PUT | /api/student/1/ | Update student |
| DELETE | /api/student/1/ | Delete student |

## Setup
git clone https://github.com/subhashdhaniyala/studentapi
cd studentapi
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
