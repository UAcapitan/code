from rest_framework import serializers
import appmain.models as models

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = ['id', 'title', 'text', 'date_of_save', 'image', 'video', 'likes']