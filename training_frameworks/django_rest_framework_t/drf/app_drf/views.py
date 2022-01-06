from rest_framework import generics
from rest_framework.response import Response
from app_drf.serializers import CarDetailSerializer, CarListSerializer, UserDetailSerializer
from app_drf.models import Car
from django.contrib.auth.models import User
from app_drf.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

    def post(self, request):
        return Response({'Text':'Success'})

class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )

class UserListView(generics.ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser, )

class UserDeleteView(generics.DestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)