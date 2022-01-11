from rest_framework import generics
from movies import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.models import Movie, Review, Genre
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser

class MovieCreateView(generics.CreateAPIView):
    serializer_class = serializers.MovieDetailedSerialize

class UserListView(generics.ListAPIView):
    serializer_class = serializers.UserListSerialize
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)

class MovieListView(APIView):
    def get(self, request):
        movies = Movie.objects.filter(id__gte=1)
        serializer = serializers.MovieListSerialize(movies, many=True)
        return Response(serializer.data)

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

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer

class GenreCreateView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = serializers.GenreDetialSerializer

class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreListSeriliazer

class MovieListAllView(generics.ListAPIView):
    serializer_class = serializers.MovieListAllSerialize
    queryset = Movie.objects.all()