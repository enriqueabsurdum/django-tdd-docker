"""Movies tests views."""

# Third party libraries
import pytest

# Models
from apps.movies.models import Movie


@pytest.mark.django_db
def test_add_movie(client):
    """Test add movie."""

    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        path='/api/movies/',
        data={
            'title': 'The Big Lebowski',
            'genre': 'Comedy',
            'year': '1998'
        },
        content_type='application/json'
    )

    assert resp.status_code == 201
    assert resp.data['title'] == 'The Big Lebowski'

    movies = Movie.objects.all()
    assert len(movies) == 1


@pytest.mark.django_db
def test_get_single_movie(client, add_movie):
    """Test get single movie."""

    movie = add_movie(
        title='The Big Lebowski',
        genre='Comedy',
        year='1998'
    )

    resp = client.get(path=f'/api/movies/{movie.id}/')

    assert resp.status_code == 200
    assert resp.data['title'] == 'The Big Lebowski'


def test_get_single_movie_incorrect_id(client):
    resp = client.get(f'/api/movies/foo/')
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    movie_one = add_movie(
        title='The Big Lebowski',
        genre='Comedy',
        year='1998'
    )
    movie_two = add_movie(
        title='No Country for Old Men',
        genre='Thriller',
        year='2007'
    )
    resp = client.get(f'/api/movies/')

    assert resp.status_code == 200
    assert resp.data[1]['title'] == movie_one.title
    assert resp.data[0]['title'] == movie_two.title


@pytest.mark.django_db
def test_remove_movie(client, add_movie):
    movie = add_movie(
        title='The Big Lebowski',
        genre='Comedy',
        year='1998'
    )

    resp = client.get(path=f'/api/movies/{movie.id}/')
    assert resp.status_code == 200
    assert resp.data['title'] == 'The Big Lebowski'

    resp_two = client.delete(path=f'/api/movies/{movie.id}/')
    assert resp_two.status_code == 204

    resp_three = client.get(path='/api/movies/')
    assert resp_three.status_code == 200
    assert len(resp_three.data) == 0


@pytest.mark.django_db
def test_remove_movie_incorrect_id(client):
    resp = client.delete(path=f'/api/movies/99/')
    assert resp.status_code == 404