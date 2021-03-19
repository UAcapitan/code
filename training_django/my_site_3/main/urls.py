from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('delete/<int:index_task>/', views.delete, name='delete'),
]