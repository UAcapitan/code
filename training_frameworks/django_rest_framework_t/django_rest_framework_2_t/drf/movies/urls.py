from django.urls import path
from movies.views import MovieCreateView

urlpatterns = [
    path('movie/create/', MovieCreateView.as_view()),
]
