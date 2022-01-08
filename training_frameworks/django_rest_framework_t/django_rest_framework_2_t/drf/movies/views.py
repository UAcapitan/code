from rest_framework import generics
from rest_framework import response
from movies.serializers import MovieDetailedSerialize, MovieListSerialize, UserListSerialize, \
    MovieDetailSerializer, UserDetailSerialize, ReviewDetailSerializer, \
    ReviewListSerialize, MovieListWithReviewsSerialize, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from movies.models import Movie, Review
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

class UserDetailView(APIView):
    def get(self, request, pk):
        users = User.objects.get(id=pk)
        serializer = UserDetailSerialize(users)
        return Response(serializer.data)

class ReviewCreateView(APIView):
    def post(self, request):
        review = ReviewDetailSerializer(data=request.data, context={"request": request})
        if review.is_valid():
            review.save()
        return Response(review.data, status=201)

class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewListSerialize
    queryset = Review.objects.all()

class MovieListWithReviewsView(generics.ListAPIView):
    serializer_class = MovieListWithReviewsSerialize
    queryset = Movie.objects.all()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer