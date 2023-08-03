from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dish, Comment
import requests
import webbrowser
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from django.urls import reverse_lazy



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
    comments = Comment.objects.filter(dish_id=dish_id)
    print(comments)
    return render(request, 'dishes/detail.html', {'dish': dish,'comments': comments})
    
    

@login_required
def dishes_index(request):
    dishes = Dish.objects.filter(user=request.user)
    return render(request, 'dishes/index.html', {'dishes': dishes})

class DishCreate(LoginRequiredMixin, CreateView):
  model = Dish
  fields = ['name', 'origin', 'description']
  success_url = '/dishes/'
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class DishUpdate(LoginRequiredMixin, UpdateView):
    model = Dish
    fields = ['origin', 'description']
    success_url = '/dishes'

class DishDelete(LoginRequiredMixin, DeleteView):
    model = Dish
    success_url = '/dishes'

def signup(request):
  error_message = ''
  if request.method == 'POST':

    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)





def comment_detail(request, food_id):
    dish = get_object_or_404(Dish, id=food_id)
    comments = dish.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.dish_id = dish
            new_comment.save()

            return redirect('detail', dish_id=dish.id)
    else:
        comment_form = CommentForm()

    context = {
        'dish': dish,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'main_app/comment_form.html', context)


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['city_name', 'restarant_name', 'body']
  

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('comment_detail')

    






    
        



