#!/bin/sh

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."

    echo $MYSQL_HOST

    echo $MYSQL_PORT

    while ! nc -z $MYSQL_HOST $MYSQL_PORT; do
      sleep 1
    done

    echo "MySQL started"
fi

python manage.py flush --no-input
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

exec "$@"