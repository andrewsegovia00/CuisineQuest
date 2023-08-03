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
    path('dish/<int:dish_id>', views.dishes_detail, name='detail'),
    # Create Dish route
    path('dish/create/', views.DishCreate.as_view(), name='dishes_create'),
    # Update Dish route
    path('dish/<int:pk>/update/', views.DishUpdate.as_view(), name='dishes_update'),
    # Delete Dish route
    path('dish/<int:pk>/delete/', views.DishDelete.as_view(), name='dishes_delete'),
    # View all dishes in favorites route
    path('mylist/', views.mylist_index, name='mylist_index'),
    # Associate a dish to my list
    path('dishes/<int:dish_id>/remove_mylist/', views.assoc_mylist, name='assoc_mylist'),
    # Unnassociate a dish to my list
    path('dishes/<int:dish_id>/add_mylist/<int:mylist_id>/', views.unassoc_mylist, name='unassoc_mylist'),
    # //potential bug due to users, sharing the same list ID, verify the user matches the id of the list's user
    # API Dish mylist
    path('add_to_favorites/<str:dish_name>/', views.add_to_my_list, name='add_to_my_list'),
    path('remove_from_favorites/<int:dish_id>/', views.remove_from_my_list, name='remove_from_my_list'),
    
    # Create comments
    path('dish/comment/<int:pk>/', views.CommentCreateView.as_view(), name='create_comment'),
    # Update comments
    path('dish/comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    # Delete comments
    path('dish/comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    # Sign up route
    path('accounts/signup/', views.signup, name='signup'),
]