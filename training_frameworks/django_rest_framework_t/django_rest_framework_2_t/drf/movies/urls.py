from django.urls import path
from movies import views
from movies import api

urlpatterns = [
    path('movie/create/', views.MovieCreateView.as_view()),
    path('movie/all/', views.MovieListView.as_view()),
    path('movie/all-full/', views.MovieListAllView.as_view()),
    path('movie/<int:pk>/', views.MovieDetailView.as_view()),

    path('review/create/', views.ReviewCreateView.as_view()),
    path('review/all/', views.ReviewListView.as_view()),

    path('genre/create/', views.GenreCreateView.as_view()),
    path('genre/all/', views.GenreListView.as_view()),

    path('users/all/', views.UserListView.as_view()),
    path('users/<int:pk>/', views.UserDetailView.as_view()),

    path('auth/oauth/login/', views.SocialLoginView.as_view()),

    path('viewset/movie/all/', api.MovieViewSet.as_view({'get':'list'})),
    path('viewset/movie/<int:pk>/', api.MovieViewSet.as_view({'get':'retrieve'})),
]