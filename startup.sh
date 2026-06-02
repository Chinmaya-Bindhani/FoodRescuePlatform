#!/bin/sh
set -e

echo "Running migrations..."
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Starting server..."
gunicorn food_rescue_project.wsgi
