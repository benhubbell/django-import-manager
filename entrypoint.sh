#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi

# if [ "$APP_ENV" = "dev" ]
# then
# pwd
# ls ./src/django_import_manager
# python src/django_import_manager/manage.py flush --no-input
# echo "before migrate"
# python src/django_import_manager/manage.py migrate
# echo "after migrate"
# fi

python manage.py flush --no-input
python manage.py migrate
python manage.py collectstatic

exec "$@"
