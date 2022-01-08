from django.urls import path
from movies.views import MovieCreateView, MovieListView, UserListView, MovieDetailView, \
    UserDetailView, ReviewCreateView, MovieListWithReviewsView, ReviewListView, \
    GenreCreateView, GenreListView, MovieListWithAllView

urlpatterns = [
    path('movie/create/', MovieCreateView.as_view()),
    path('movie/all/', MovieListView.as_view()),
    path('movie/<int:pk>/', MovieDetailView.as_view()),
    path('movie/list/', MovieListWithReviewsView.as_view()),
    path('movie/list/all', MovieListWithAllView.as_view()),

    path('review/create/', ReviewCreateView.as_view()),
    path('review/all/', ReviewListView.as_view()),

    path('genre/create/', GenreCreateView.as_view()),
    path('genre/all/', GenreListView.as_view()),

    path('users/all/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
]
