#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py migrate --database=db
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'djangotestpw')" | python manage.py shell