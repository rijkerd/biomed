#!/bin/sh

if [ "$DATABASE_NAME" = "postgres" ]
then
    echo "Waiting for postgres..."

    echo $DATABASE_HOST

    echo $DATABASE_PORT

    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
      sleep 0.5
    done

    echo "Postgres started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py runserver

exec "$@"