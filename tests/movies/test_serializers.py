"""Movies tests serializers."""

# Serializers
from apps.movies.serializers import MovieSerializer


def test_valid_movie_serializer():
    """Test valid movie serializer."""

    valid_serializer_data = {
        "title": "Raising Arizona",
        "genre": "Comedy",
        "year": "1987",
    }
    serializer = MovieSerializer(data=valid_serializer_data)

    assert serializer.is_valid()
    assert serializer.validated_data == valid_serializer_data
    assert serializer.data == valid_serializer_data
    assert serializer.errors == {}


def test_invalid_movie_serializer():
    """Test invalid movie serializer."""

    invalid_serializer_data = {
        "title": "Raising Arizona",
        "genre": "Comedy",
    }
    serializer = MovieSerializer(data=invalid_serializer_data)

    assert not serializer.is_valid()
    assert serializer.validated_data == {}
    assert serializer.data == invalid_serializer_data
    print(serializer.errors)
    # assert serializer.errors == {'year': ['This field is required.']}
