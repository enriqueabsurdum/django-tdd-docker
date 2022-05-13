"""Movies tests factory as fixture."""

# Third party libraries
import pytest

# Models
from apps.movies.models import Movie


@pytest.fixture(scope='function')
def add_movie():
    """Add movie."""

    def _add_movie(title, genre, year):
        movie = Movie.objects.create(
            title=title,
            genre=genre,
            year=year
        )
        return movie

    return _add_movie
