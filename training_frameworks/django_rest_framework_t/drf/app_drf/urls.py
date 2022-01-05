from django.urls import path
from app_drf.views import CarCreateView, CarListView, CarDetailView

urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('car/all/', CarListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),
]