"""
WSGI config for mymind project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

from mymind.wsgi import MyMindApplication
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mymind.settings")

application = get_wsgi_application()

application = MyMindApplication(application)
