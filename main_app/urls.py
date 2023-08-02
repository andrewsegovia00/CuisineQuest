from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('daily_dish/', views.daily_dish, name='daily_dish'),
    path('dishes/', views.dishes_index, name='index'),
    path('dishes_list/', views.dishes_list, name='dishes'),
    path('dishes/<int:dish_id>', views.dishes_detail, name='detail'),
    path('dishes/create/', views.DishCreate.as_view(), name='dishes_create'),
    path('dishes/<int:pk>/update/', views.DishUpdate.as_view(), name='dishes_update'),
    path('dishes/<int:pk>/delete/', views.DishDelete.as_view(), name='dishes_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('<int:food_id>/', views.comment_detail, name='comment_detail'),
]