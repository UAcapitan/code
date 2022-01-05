from rest_framework import serializers
from app_drf.models import Car
from django.contrib.auth.models import User


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'

class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'vin', 'user']

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_staff']

