from rest_framework import serializers
import appmain.models as models

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'