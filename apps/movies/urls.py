"""Movies URLs."""

# Django
from django.urls import path

# Views
from apps.movies.views import MovieList, MovieDetail

urlpatterns = [
    path('api/movies/', MovieList.as_view(), name='movie_list'),
    path('api/movies/<uuid:uuid>/', MovieDetail.as_view(), name='movie_detail'),
]
