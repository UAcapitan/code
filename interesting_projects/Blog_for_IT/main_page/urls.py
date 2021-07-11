from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-article/', views.create_article, name='create_article'),
    path('articles/', views.articles, name='articles'),
    path('post/<int:id>/', views.post, name='post'),
    path('registration/', views.reg, name='reg'),
]
