from django.urls import path
import api.views as views

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('rate/', views.RateView.as_view(), name='rate'),
    path('article/<int:id>/', views.ArticleView.as_view(), name='article'),
    path('articles/names/', views.ArticleNameListView.as_view(), name='articles_names'),
    path('profile/', views.UserDataView.as_view(), name='profile'),
    path('article/delete/', views.DeleteArticleView.as_view(), name='delete_article'),
    path('article/liked/', views.FavouriteArticleView.as_view(), name='article_liked'),
    path('article/create/', views.CreateArticleView.as_view(), name='create_article'),
    path('article/comment/', views.CommentToArticleView.as_view(), name='article_comment'),
    path('recommendation/', views.RecommendationView.as_view(), name='recommendation'),
    path('comments/', views.CommentListView.as_view(), name='comments'),
]