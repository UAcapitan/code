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

class DeleteArticleView(APIView):
    def post(self, request):
        id = request.data.get('id')

        try:
            id = int(id)
            models.Article.objects.get(id=id).delete()
        except:
            return Response({'status': 'Article was not deleted'})

        return Response({'status': 'Article was deleted'}, status=200)

class FavouriteArticleView(APIView):
    def post(self, request):
        json_dict = {}
        json_dict.items
        user_token = request.data.get('token')

        try:
            token = Token.objects.get(key=user_token)
            articles = models.Like.objects.filter(user=token.user)
            json_dict["article"] = [article.article.title for article in articles]
        except Exception as e:
            json_dict["error"] = str(e)

        return Response(json_dict)

class CreateArticleView(APIView):
    permission_classes = (IsAdminUser,)
    def post(self, request):
        json_dict = {}
        user_token = request.data.get('token')
        print(request.data)

        try:
            token = Token.objects.get(key=user_token)
            user = User.objects.get(username=token.user)
            model = models.Article(
                title=request.data.get('title'),
                text=request.data.get('text'),
                user=user,
                video=request.data.get('video'),
            )
            model.save()
            json_dict["article"] = {
                'id': model.id,
                'title': model.title,
                'text': model.text,
                'user': model.user.username,
                'date_of_user': model.date_of_save,
                'image': 'None, please install image via admin menu',
                'video': model.video,
                'likes': model.likes,
            }
        except Exception as e:
            json_dict["error"] = str(e)

        return Response(json_dict)

class CommentToArticleView(APIView):
    def post(self, request):
        json_dict = {}
        user_token = request.data.get('token')

        try:
            token = Token.objects.get(key=user_token)
            user = User.objects.get(username=token.user)
            article = models.Article.objects.get(id=int(request.data.get('id')))
            model = models.Comment(
                text=request.data.get('text'),
                user=user,
                article=article,
            )
            model.save()
            json_dict["comment"] = {
                'id': model.id,
                'title': model.text,
                'user': model.user.username,
                'article': model.article.title,
                'date': model.date,
            }
        except Exception as e:
            json_dict["error"] = str(e)

        return Response(json_dict)

class RecommendationView(APIView):
    def get(self, request):
        article = models.Recommendation.objects.get(pk=1)
        model = article.article
        json_dict = {
                'id': model.id,
                'title': model.title,
                'text': model.text,
                'user': model.user.username,
                'date_of_user': model.date_of_save,
                'image': 'None, please install image via admin menu',
                'video': model.video,
                'likes': model.likes,
            }
        return Response(json_dict)

class CommentListView(generics.ListAPIView):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all().order_by('-id')
    pagination_class = service.PagonationArticlePageSize10
    permission_classes = (IsAdminUser,)