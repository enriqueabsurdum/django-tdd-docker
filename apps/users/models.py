"""Users models."""

# Django
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom user model class."""

    pass
