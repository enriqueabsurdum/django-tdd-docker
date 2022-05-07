"""Users apps."""

# Django
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Users config model class."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'
