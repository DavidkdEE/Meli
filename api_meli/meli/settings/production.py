from .base import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DJANGO_POSTGRES_DATABASE'),
        'USER': os.environ.get('DJANGO_POSTGRES_USER'),
        'PASSWORD': os.environ.get('DJANGO_POSTGRES_PASSWORD'),
        'HOST': os.environ.get('DJANGO_POSTGRES_HOST'),
        'PORT': os.environ.get('DJANGO_POSTGRES_PORT'),
    }
}
