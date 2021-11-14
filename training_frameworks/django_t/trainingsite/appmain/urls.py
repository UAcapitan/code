from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('article/<int:id>/', article, name='article'),
    re_path(r'^year/(?P<year>[0-9]{4})/', year),
    path('articles/', articles, name='articles')
]