"""Movies serializers."""

# Django REST framework
from rest_framework import serializers

# Models
from apps.movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Movie serializer model class."""

    class Meta:
        """Meta options."""

        model = Movie
        fields = "__all__"
        read_only_fields = ("pk_id", "id", "created", "modified")
