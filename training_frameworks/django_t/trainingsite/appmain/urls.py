from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', ArticleMain.as_view(), name='main'),
    path('article/<slug:slug>/', ShowPage.as_view(), name='article'),
    re_path(r'^year/(?P<year>[0-9]{4})/', year),
    path('articles/', articles, name='articles'),
    path('category/<slug:id>/', CategoryPage.as_view(), name='category'),
    path('form-page/', FormPage.as_view(), name='form_page'),
    path('orm/', orm_commands, name='orm_commands'),
    path('reg/', reg, name='reg')
]