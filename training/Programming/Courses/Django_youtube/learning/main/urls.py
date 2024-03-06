
from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name="main"),
    path('/only-text', views.index, name="text")
]