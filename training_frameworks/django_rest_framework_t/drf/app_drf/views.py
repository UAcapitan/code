from django.shortcuts import render
from rest_framework import generics, serializers
from app_drf.serializers import CarDetailSerializer, CarListSerializer
from app_drf.models import Car

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()