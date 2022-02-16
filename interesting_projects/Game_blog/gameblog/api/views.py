from rest_framework import generics
import api.serializers as serializers
from rest_framework.permissions import IsAdminUser
import appmain.models as models
import api.service as service
from rest_framework.views import APIView
from rest_framework.response import Response

class ArticleListView(generics.ListAPIView):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all().order_by('-id')
    pagination_class = service.PaginationArticle

class RateView(generics.ListAPIView):
    serializer_class = serializers.RateSerializer
    queryset = models.Article.objects.all().order_by('-likes')[:10]

class ArticleView(APIView):
    def get(self, request, id):
        movies = models.Article.objects.filter(id=id)
        serializer = serializers.ArticleSerializer(movies, many=True)
        return Response(serializer.data)