from django.urls import path
from . import views

urlpatterns = [
    # Home route
    path('', views.home, name='home'),
    # Random Dish route
    path('daily_dish/', views.daily_dish, name='daily_dish'),
    # View all Dishes from user
    path('dishes/', views.dishes_index, name='index'),
    # View all Dishes from API
    path('dishes_list/', views.dishes_list, name='dishes'),
    # View one dish
    path('dishes/<int:dish_id>', views.dishes_detail, name='detail'),
    # Create Dish route
    path('dishes/create/', views.DishCreate.as_view(), name='dishes_create'),
    # Update Dish route
    path('dishes/<int:pk>/update/', views.DishUpdate.as_view(), name='dishes_update'),
    # Delete Dish route
    path('dishes/<int:pk>/delete/', views.DishDelete.as_view(), name='dishes_delete'),
    # View all dishes in favorites route
    path('mylist/', views.mylist_index, name='mylist_index'),
    # Associate a dish to my list
    path('dishes/<int:dish_id>/assoc_mylist/', views.assoc_mylist, name='assoc_mylist'),
    # Unnassociate a dish to my list
    path('dishes/<int:dish_id>/unassoc_mylist/<int:mylist_id>/', views.unassoc_mylist, name='unassoc_mylist'),
    # Sign up route
    path('accounts/signup/', views.signup, name='signup'),

]