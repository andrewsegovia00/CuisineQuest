from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('daily_dish/', views.daily_dish, name='daily_dish'),
    path('dishes/', views.dishes, name='dishes'),
]