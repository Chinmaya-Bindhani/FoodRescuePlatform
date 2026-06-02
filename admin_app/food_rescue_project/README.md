# Food Rescue Project

Minimal Django Food Rescue project with:
- Home, About, Login, Admin navbar
- Register -> redirect back to Login
- Login -> Dashboard
- Human Food page
- Separate Human Veg page
- Separate Human Non-Veg page
- Separate Animal Food page
- Add Donation Item form
- Django Admin support
- Black and white minimal design

## Run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Login/Register Flow
- Open `/login/`
- If not registered, click Register
- After register, it returns to Login page
- After login, it opens Dashboard

## Important
Default database is SQLite so project works immediately.
MySQL config sample is already added inside `food_rescue/settings.py`.
