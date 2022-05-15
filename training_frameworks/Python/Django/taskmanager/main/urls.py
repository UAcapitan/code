from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('page', views.page, name='page'),
    path('create', views.create, name='create')
]