"""Movies views."""

# Django
from django.http import Http404

# Django REST framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Third party libraries
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Models
from apps.movies.models import Movie

# Serializers
from apps.movies.serializers import MovieSerializer


class MovieList(APIView):
    """Movie list model class."""

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "genre": openapi.Schema(type=openapi.TYPE_STRING),
                "year": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    """Movie detail model class."""

    def get_object(self, uuid):
        try:
            return Movie.objects.get(id=uuid)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, uuid, format=None):
        movie = self.get_object(uuid)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "genre": openapi.Schema(type=openapi.TYPE_STRING),
                "year": openapi.Schema(type=openapi.TYPE_STRING),
            },
        )
    )
    def put(self, request, uuid, format=None):
        movie = self.get_object(uuid)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        movie = self.get_object(uuid)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
