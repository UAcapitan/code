from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from movies import models
from movies import serializers

class MovieViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = models.Movie.objects.all()
        serializer = serializers.MovieListSerialize(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = serializers.MovieDetailedSerialize(movie)
        return Response(serializer.data)