from .base import *

from datetime import timedelta
import os

_SECRET_KEY = '60ywntmm#$yjosvsdaakb2&q7m+=!86nshya5cfo_(e4lugo6+'
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', _SECRET_KEY)

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60*24)
}
