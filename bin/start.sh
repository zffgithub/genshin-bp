#! /bin/bash
.env/bin/python manage.py runserver 0.0.0.0:8443
# gunicorn banpick.asgi -c bin/gunicorn_config.py