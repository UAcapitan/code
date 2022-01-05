from django.urls import path

from app_drf.views import CarCreateView

urlpatterns = [
    path('car/create/', CarCreateView.as_view())
]