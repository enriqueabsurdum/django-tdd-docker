"""Users admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserModel

# Models
from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(DefaultUserModel):
    """Custom user admin model class."""

    pass
