"""Movies apps."""

# Django
from django.apps import AppConfig


class MoviesConfig(AppConfig):
    """Movies config model class."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.movies'
