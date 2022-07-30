"""
WSGI config for meli project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from werkzeug.middleware.proxy_fix import ProxyFix

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meli.settings')

application = get_wsgi_application()
application = ProxyFix(application, x_for=1, x_host=1, x_port=1)
