from rest_framework import generics
import api.serializers as serializers
from rest_framework.permissions import IsAdminUser
import appmain.models as models
import api.service as service
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

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

class ArticleNameListView(generics.ListAPIView):
    serializer_class = serializers.NameOfArticlesSerializer
    queryset = models.Article.objects.all().order_by('-id')
    pagination_class = service.PagonationArticlePageSize10

class UserDataView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        json_dict = {}
        user_token = request.data.get('token')

        try:
            token = Token.objects.get(key=user_token)
            user = User.objects.get(username=token.user)
            json_dict["id"] = user.id
            json_dict["username"] = user.username
            json_dict["email"] = user.email
        except Exception as e:
            json_dict["error"] = str(e)

        return Response(json_dict)

        