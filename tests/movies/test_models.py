"""Movies tests models."""

# Third party libraries
import pytest

# Models
from apps.movies.models import Movie


@pytest.mark.django_db
def test_movie_model():
    """Test movie model."""

    movie = Movie(
        title='Raising Arizona',
        genre='comedy',
        year='1987'
    )
    movie.save()

    assert movie.title == 'Raising Arizona'
    assert movie.genre == 'comedy'
    assert movie.year == '1987'
    assert movie.created
    assert movie.modified
    assert str(movie) == movie.title
