from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create-article/', views.create_article, name='create_article'),
]
