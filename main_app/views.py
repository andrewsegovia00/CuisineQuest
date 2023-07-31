from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dish
import requests
import webbrowser

# Create your views here.
def home(request):
    return render(request, 'home.html')

def daily_dish(request):
    api_url = "https://www.themealdb.com/api/json/v1/1/random.php"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        dish = data['meals'][0]

        dish_name = dish['strMeal']
        dish_picture_url = dish['strMealThumb']

        context = {
            'dish_name': dish_name,
            'dish_picture_url': dish_picture_url,
        }

        return render(request, 'dishes/daily_dish.html', context)
    else:
        return render(request, 'error.html') 

    
def dishes_list(request):
    api_url = "https://www.themealdb.com/api/json/v1/1/random.php"

    random_meals = []

    for _ in range(4):
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            random_meal = data['meals'][0]
            random_meals.append(random_meal)
    
    return render(request, 'dishes/dishes.html', {'random_meals': random_meals})

def dishes_detail(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    return render(request, 'dishes/detail.html', {'dish': dish})

def dishes_index(request):
    dishes = Dish.objects.all()
    return render(request, 'dishes/index.html', {'dishes': dishes})

class DishCreate(CreateView):
  model = Dish
  fields = ['name', 'origin', 'description']
  success_url = '/dishes/'

class DishUpdate(UpdateView):
    model = Dish
    fields = ['origin', 'description']
    success_url = '/dishes'

class DishDelete(DeleteView):
    model = Dish
    success_url = '/dishes'