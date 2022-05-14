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
        path="/api/movies/",
        data={
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": "1998",
        },
        content_type="application/json",
    )

    assert resp.status_code == 201
    assert resp.data["title"] == "The Big Lebowski"

    movies = Movie.objects.all()
    assert len(movies) == 1


@pytest.mark.django_db
def test_get_single_movie(client, add_movie):
    """Test get single movie."""

    movie = add_movie(
        title="The Big Lebowski",
        genre="comedy",
        year="1998",
    )

    resp = client.get(path=f"/api/movies/{movie.id}/")

    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"


def test_get_single_movie_incorrect_id(client):
    """Test get single movie incorrect id."""

    resp = client.get("/api/movies/foo/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    """Test get all movies."""

    movie_one = add_movie(
        title="The Big Lebowski",
        genre="comedy",
        year="1998",
    )
    movie_two = add_movie(
        title="No Country for Old Men",
        genre="Thriller",
        year="2007",
    )
    resp = client.get("/api/movies/")

    assert resp.status_code == 200
    assert resp.data[1]["title"] == movie_one.title
    assert resp.data[0]["title"] == movie_two.title


@pytest.mark.django_db
def test_remove_movie(client, add_movie):
    """Test remove movies."""

    movie = add_movie(
        title="The Big Lebowski",
        genre="comedy",
        year="1998",
    )

    resp = client.get(path=f"/api/movies/{movie.id}/")
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"

    resp_two = client.delete(path=f"/api/movies/{movie.id}/")
    assert resp_two.status_code == 204

    resp_three = client.get(path="/api/movies/")
    assert resp_three.status_code == 200
    assert len(resp_three.data) == 0


@pytest.mark.django_db
def test_remove_movie_incorrect_id(client):
    """Test remove movie incorrect id."""

    resp = client.delete(path="/api/movies/99/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_movie(client, add_movie):
    """Test update movie."""

    movie = add_movie(
        title="The Big Lebowski",
        genre="comedy",
        year="1998",
    )

    resp = client.put(
        f"/api/movies/{movie.id}/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": "1997",
        },
        content_type="application/json",
    )
    assert resp.status_code == 200
    assert resp.data["title"] == "The Big Lebowski"
    assert resp.data["year"] == "1997"

    resp_two = client.get(f"/api/movies/{movie.id}/")
    assert resp_two.status_code == 200
    assert resp_two.data["title"] == "The Big Lebowski"
    assert resp.data["year"] == "1997"


@pytest.mark.django_db
def test_update_movie_incorrect_id(client):
    """Test update movie incorrect id."""

    resp = client.put("/api/movies/99/")
    assert resp.status_code == 404


@pytest.mark.django_db
def test_update_movie_invalid_json(client, add_movie):
    """Test updated movie invalid json."""

    movie = add_movie(
        title="The Big Lebowski",
        genre="comedy",
        year="1998",
    )
    resp = client.put(
        f"/api/movies/{movie.id}/",
        {},
        content_type="application/json",
    )
    assert resp.status_code == 400


@pytest.mark.django_db
def test_update_movie_invalid_json_keys(client, add_movie):
    """Test update movie invalid json keys."""

    movie = add_movie(
        title="The Big Lebowski",
        genre="comedy",
        year="1998",
    )

    resp = client.put(
        f"/api/movies/{movie.id}/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
        },
        content_type="application/json",
    )
    assert resp.status_code == 400
