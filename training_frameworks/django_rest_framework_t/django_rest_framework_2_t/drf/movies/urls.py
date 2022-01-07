from django.urls import path
from movies.views import MovieCreateView, MovieListView, UserListView, MovieDetailView

urlpatterns = [
    path('movie/create/', MovieCreateView.as_view()),
    path('movie/all/', MovieListView.as_view()),
    path('movie/<int:pk>/', MovieDetailView.as_view()),

    path('users/all/', UserListView.as_view()),
]
