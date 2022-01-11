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

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

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