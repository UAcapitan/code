from rest_framework import serializers
from movies.models import Movie, Review, Genre
from django.contrib.auth.models import User
from movies import user_token

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
        fields = ('name', 'user')

class MovieListAllSerialize(serializers.ModelSerializer):
    reviews = ReviewListSerialize(many=True)
    genre = GenreListSeriliazer()

    class Meta:
        model = Movie
        fields = '__all__'

class SocialSerializer(serializers.Serializer):
    '''Serializer which accepts an OAuth2 access token and provider.'''

    access_token = serializers.CharField(max_length=4096, trim_whitespace=True,
    default=user_token.TOKEN)