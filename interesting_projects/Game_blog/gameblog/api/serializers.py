from rest_framework import serializers
import appmain.models as models
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['id', 'title', 'text', 'date_of_save', 'image', 'video', 'likes']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recommendation
        fields = '__all__'

class NameOfArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['title',]