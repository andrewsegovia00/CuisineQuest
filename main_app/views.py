from django.shortcuts import render
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

        return render(request, 'daily_dish.html', context)
    else:
        return render(request, 'error.html') 
    
    
def dishes(request):
    api_url = "https://www.themealdb.com/api/json/v1/1/random.php"

    random_meals = []

    for _ in range(4):
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            random_meal = data['meals'][0]
            random_meals.append(random_meal)
    
    return render(request, 'dishes.html', {'random_meals': random_meals})