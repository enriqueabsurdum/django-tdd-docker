"""django-tdd-docker URL configuration."""

# Django
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', include('apps.common.urls')),
]
