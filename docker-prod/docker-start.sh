#!/usr/bin/env bash
set -e

# Run tests
cd .
python manage.py makemigrations
python manage.py migrate
python manage.py initadmin
rm -rf /usr/src/app/logs/
mkdir /usr/src/app/logs/
touch /usr/src/app/logs/gunicorn.log
touch /usr/src/app/logs/access.log

# exec python manage.py runserver 0.0.0.0:8000
exec gunicorn kingobet.wsgi:application --bind 0.0.0.0:8000