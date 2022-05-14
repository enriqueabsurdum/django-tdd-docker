"""Common apps."""

# Django
from django.apps import AppConfig


class CommonConfig(AppConfig):
    """Common config model class."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.common"
