
from django.urls import path
from . import views


urlpatterns = [
    path('', views.news, name="news"),
    path("create/", views.create_news, name="create_news"),
    path("<int:pk>/", views.NewsDetailView.as_view(), name="news-detail")
]