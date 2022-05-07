"""Django local settings for django-tdd-docker project."""

# Base configuration
from .base import *  # noqa

# Local configuration
# ----------------------------------------------------------------------------
SECRET_KEY = 'django-insecure-75rw_w9)2o25f^!$nhnojjlc)2h82@yy1dxp-79v2@weipe3jq'
DEBUG = True
ALLOWED_HOSTS = []

# Application definition
# ----------------------------------------------------------------------------
INSTALLED_APPS += []

# Middleware
# ----------------------------------------------------------------------------
MIDDLEWARE += []

# Database
# ----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
