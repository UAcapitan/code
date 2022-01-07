from rest_framework import generics
from movies.serializers import MovieDetailedSerialize, MovieListSerialize, UserListSerialize, \
    MovieDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.models import Movie
from django.contrib.auth.models import User

class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieDetailedSerialize

class UserListView(generics.ListAPIView):
    serializer_class = UserListSerialize
    queryset = User.objects.all()

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(id__gte=2)
        serializer = MovieListSerialize(movies, many=True)
        return Response(serializer.data)

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()
