from django.shortcuts import render
from rest_framework import generics
from app_drf.serializers import CarDetailSerializer

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
