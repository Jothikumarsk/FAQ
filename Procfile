release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn faq_list.wsgi --log-file -