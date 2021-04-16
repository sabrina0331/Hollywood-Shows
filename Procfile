web: gunicorn learning_log.wsgi:shows --log-file - --log-level debug
python manage.py colectstatic --noinput
manage.py migrate