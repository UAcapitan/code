from rest_framework import serializers
from movies.models import Movie

class MovieDetailedSerialize(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerialize(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name', 'text',]