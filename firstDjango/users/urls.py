from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_year, name='user_year'),
    path('user/search', views.user_by_year, name='user_by_year'),
]