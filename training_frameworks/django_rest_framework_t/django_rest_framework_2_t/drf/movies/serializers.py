from rest_framework import serializers
from movies.models import Movie
from django.contrib.auth.models import User

class MovieDetailedSerialize(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerialize(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'text',)

class UserListSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ('id', 'user')

class UserDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')