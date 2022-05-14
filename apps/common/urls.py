"""Common URLs."""

# Django
from django.urls import path

# Views
from apps.common.views import ping_pong

urlpatterns = [
    path("", ping_pong, name="ping"),
]
