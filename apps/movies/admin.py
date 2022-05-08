"""Movies admin."""

# Django
from django.contrib import admin

# Models
from apps.movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Movie admin model class."""

    fields = ('title', 'genre', 'year', 'created', 'modified')
    list_display = ('title', 'genre', 'year')
    readonly_fields = ('created', 'modified')
