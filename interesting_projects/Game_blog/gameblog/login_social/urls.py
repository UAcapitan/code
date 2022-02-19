from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_page, name='login_social'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout_social"),
    path('social-auth/', include('social_django.urls', namespace="social")),
]