from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('reg/', views.reg, name='reg'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile')
]