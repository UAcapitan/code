from rest_framework import generics
from movies import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.models import Movie, Review, Genre
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from movies.service import MovieAllFilter, ReviewFilter, MovieFilter

class MovieCreateView(generics.CreateAPIView):
    serializer_class = serializers.MovieDetailedSerialize

class UserListView(APIView):
    permission_classes = (IsAdminUser,)
    def get(self, request):
        users = User.objects.all()
        serializer = serializers.UserListSerialize(users, many=True)
        return Response(serializer.data)

class MovieListView(generics.ListAPIView):
    serializer_class = serializers.MovieListSerialize
    queryset = Movie.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MovieDetailSerializer
    queryset = Movie.objects.all()

class UserDetailView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serialier_class = serializers.UserDetailSerialize

class ReviewCreateView(APIView):
    def post(self, request):
        review = serializers.ReviewDetailSerializer(data=request.data, context={"request": request})
        if review.is_valid():
            review.save()
        return Response(review.data, status=201)

class ReviewListView(generics.ListAPIView):
    serializer_class = serializers.ReviewListSerialize
    queryset = Review.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReviewFilter

class GenreCreateView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = serializers.GenreDetialSerializer

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreListSeriliazer

class MovieListAllView(generics.ListAPIView):
    serializer_class = serializers.MovieListAllSerialize
    queryset = Movie.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieAllFilter