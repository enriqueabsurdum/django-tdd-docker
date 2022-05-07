"""
WSGI config for django-tdd-docker project.
It exposes the WSGI callable as a module-level variable named ``application``.
"""

# Standard libraries
import os

# Django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

application = get_wsgi_application()
