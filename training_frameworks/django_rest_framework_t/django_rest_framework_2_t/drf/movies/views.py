from rest_framework import generics, permissions, status
from movies import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from movies import models
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from movies import service
from requests.exceptions import HTTPError
from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
from django.contrib.auth import login
from rest_framework.authtoken.models import Token

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
    queryset = models.Movie.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = service.MovieFilter

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MovieDetailedSerialize
    queryset = models.Movie.objects.all()

class UserDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = serializers.UserDetailSerialize
    queryset = User.objects.all()

class ReviewCreateView(APIView):
    def post(self, request):
        review = serializers.ReviewDetailSerializer(data=request.data, context={"request": request})
        if review.is_valid():
            review.save()
        return Response(review.data, status=201)

class ReviewListView(generics.ListAPIView):
    serializer_class = serializers.ReviewListSerialize
    queryset = models.Review.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = service.ReviewFilter

class GenreCreateView(generics.CreateAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = serializers.GenreDetialSerializer

class GenreListView(generics.ListAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreListSeriliazer

class MovieListAllView(generics.ListAPIView):
    '''Output all information about movies'''

    serializer_class = serializers.MovieListAllSerialize
    queryset = models.Movie.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = service.MovieAllFilter

class SocialLoginView(generics.GenericAPIView):
    """Log in using facebook"""
    serializer_class = serializers.SocialSerializer
    permission_classes = [permissions.AllowAny]
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = 'facebook'
        strategy = load_strategy(request)
 
        try:
            backend = load_backend(strategy=strategy, name=provider,
            redirect_uri=None)
 
        except MissingBackend:
            return Response({'error': 'Please provide a valid provider'},
            status=status.HTTP_400_BAD_REQUEST)
        try:
            if isinstance(backend, BaseOAuth2):
                access_token = serializer.data.get('access_token')
            user = backend.do_auth(access_token)
        except HTTPError as error:
            return Response({
                "error": {
                    "access_token": "Invalid token",
                    "details": str(error)
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        except AuthTokenError as error:
            return Response({
                "error": "Invalid credentials",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)
 
        try:
            authenticated_user = backend.do_auth(access_token, user=user)
        
        except HTTPError as error:
            return Response({
                "error":"invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except AuthForbidden as error:
            return Response({
                "error":"invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)
 
        if authenticated_user and authenticated_user.is_active:
            login(request, authenticated_user)
            token = Token.objects.get_or_create(user=user)[0]
            response_data = {
                'username': authenticated_user.username,
                'token': str(token),
            }

            return Response(status=status.HTTP_200_OK, data=response_data)