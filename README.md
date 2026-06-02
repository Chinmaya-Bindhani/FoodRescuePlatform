# Food Rescue System

## Stack
- Frontend: HTML, CSS, JS
- Backend: Django + Python
- Database: MySQL

## Apps
- home_app
- about_app
- register_app
- login_app
- donation_app
- human_food_app
- animal_food_app
- admin_app

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## MySQL
Create database:
```sql
CREATE DATABASE food_rescue_db;
```

Then open `food_rescue_project/settings.py` and change:
- `USER`
- `PASSWORD`
- `HOST`
- `PORT`

## Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Main URLs
- `/` home
- `/about/`
- `/register/`
- `/login/`
- `/donate/`
- `/human-food/`
- `/animal-food/`
- `/admin-page/`
- `/django-admin/`
"# FoodRescuePlatform" 
