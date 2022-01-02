from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('reg/', views.reg, name='reg'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('article/<int:id>/', views.article, name='article'),
    path('favourite/', views.favourite, name='favourite'),
    path('rate/', views.rate, name='rate'),
    path('list-of-article/', views.list_of_articles, name='list_of_articles'),
    path('add-article/', views.add_article, name='add_article'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('set-recommendation/', views.set_recommendation, name='set_recommendation'),
    path('admin-page/', views.admin_page, name='admin_page'),
    path('add-in-favourite/<int:id>', views.add_in_favourite, name='add_in_favourite')
]