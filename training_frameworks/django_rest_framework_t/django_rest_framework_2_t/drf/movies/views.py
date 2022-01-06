from rest_framework import generics
from movies.serializers import MovieDetailedSerialize

class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieDetailedSerialize
