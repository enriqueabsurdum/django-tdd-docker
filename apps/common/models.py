"""Common models."""

# Standard libraries
import uuid

# Django
from django.db import models


class BaseModel(models.Model):
    """Base model class."""

    pk_id = models.BigAutoField(
        primary_key=True,
        editable=False,
    )
    id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options."""

        abstract = True
        ordering = ("-created", "-modified")
