from rest_framework import generics
import api.serializers as serializers
import appmain.models as models

class ArticleListView(generics.ListAPIView):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()