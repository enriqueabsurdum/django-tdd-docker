"""django-tdd-docker URL configuration."""

# Django
from django.contrib import admin
from django.urls import include, path

# Django REST framework
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

# Third party libraries
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Movies API",
        default_version="v1",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ping/", include("apps.common.urls")),
    path("", include("apps.movies.urls")),
    # Swagger configuration
    path(
        "swagger-docs/",
        schema_view.with_ui(
            "swagger",
            cache_timeout=0,
        ),
        name="schema-swagger-ui",
    ),
    path("docs/", include_docs_urls(title="Movies API")),
]
