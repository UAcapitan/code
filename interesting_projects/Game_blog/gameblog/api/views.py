from rest_framework import generics
import api.serializers as serializers
from rest_framework.permissions import IsAdminUser
import appmain.models as models
import api.service as service

class ArticleListView(generics.ListAPIView):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all().order_by('-id')
    pagination_class = service.PaginationArticle

class RateView(generics.ListAPIView):
    serializer_class = serializers.RateSerializer
    queryset = models.Article.objects.all().order_by('-likes')[:10]

class ArticleCreateView(generics.CreateAPIView):
    serializer_class = serializers.ArticleSerializer
    permission_classes = (IsAdminUser,)