"""Django local settings for django-tdd-docker project."""

# Standard libraries
import os

# Base configuration
from config.settings.base import *  # noqa

# Local configuration
# ----------------------------------------------------------------------------
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split()

# Application definition
# ----------------------------------------------------------------------------
INSTALLED_APPS += []  # noqa

# Middleware
# ----------------------------------------------------------------------------
MIDDLEWARE += []  # noqa

# Database
# ----------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),  # noqa
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}
