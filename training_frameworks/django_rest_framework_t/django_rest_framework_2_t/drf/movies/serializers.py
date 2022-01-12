from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from movies.models import Movie, Review, Genre
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class MovieDetailedSerialize(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerialize(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'text',)

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ('id', 'user')

class UserListSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class UserDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ReviewDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = '__all__'

class ReviewListSerialize(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'user')

class GenreListSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class GenreDetialSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Genre
        fields = ('name',)

class MovieListAllSerialize(serializers.ModelSerializer):
    reviews = ReviewListSerialize(many=True)
    genre = GenreListSeriliazer()

    class Meta:
        model = Movie
        fields = '__all__'