"""
ASGI config for django-tdd-docker project.
It exposes the ASGI callable as a module-level variable named ``application``.
"""

# Standard libraries
import os

# Django
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

application = get_asgi_application()
