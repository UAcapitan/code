from django.urls import path
from movies import views

urlpatterns = [
    path('movie/create/', views.MovieCreateView.as_view()),
    path('movie/all/', views.MovieListView.as_view()),
    path('movie/<int:pk>/', views.MovieDetailView.as_view()),
    path('movie/list/', views.MovieListWithReviewsView.as_view()),
    path('movie/list/all', views.MovieListWithAllView.as_view()),

    path('review/create/', views.ReviewCreateView.as_view()),
    path('review/all/', views.ReviewListView.as_view()),

    path('genre/create/', views.GenreCreateView.as_view()),
    path('genre/all/', views.GenreListView.as_view()),

    path('users/all/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),
]
