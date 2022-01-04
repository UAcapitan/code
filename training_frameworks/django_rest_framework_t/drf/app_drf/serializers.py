from django.db.models import fields
from rest_framework import serializers
from app_drf.models import Car

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'