from django.urls import path
from app_drf.views import CarCreateView, CarListView, CarDetailView, UserListView, UserDeleteView

urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('car/all/', CarListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),
    path('user/all/', UserListView.as_view()),
    path('user/delete/<int:pk>/', UserDeleteView.as_view()),
]