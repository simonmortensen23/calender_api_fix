release: python manage.py makemigrations && python manage.py migrate

web: gunicorn calender_api.wsgi
