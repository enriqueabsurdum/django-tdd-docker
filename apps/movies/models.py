"""Movies models."""

# Django
from django.db import models

# Base
from apps.common.models import BaseModel


class Movie(BaseModel):
    """Movie model class."""

    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.CharField(max_length=4)

    def __str__(self):
        """Returns title field."""
        return self.title
