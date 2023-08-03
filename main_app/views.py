from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dish, MyList, APIDish, APIList, Comment
import requests
import webbrowser
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Returns Home template
def home(request):
    return render(request, 'home.html')

# Returns random daily dish
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

# Returns a detail page for an API dish
def dishes_list(request):
    api_url = "https://www.themealdb.com/api/json/v1/1/categories.php"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        categories = [category['strCategory'] for category in data['categories']]
    else:
        categories = []

    selected_category = request.GET.get('category')

    if selected_category:
        selected_api_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={selected_category}"
        response = requests.get(selected_api_url)
        
        if response.status_code == 200:
            data = response.json()
            random_meals = data['meals'][:4]
        else:
            random_meals = []
    else:
        # Fetch four random meals from the API as the default list
        random_api_url = "https://www.themealdb.com/api/json/v1/1/random.php"
        random_meals = []
        for _ in range(4):
            response = requests.get(random_api_url)
            if response.status_code == 200:
                data = response.json()
                random_meal = data['meals'][0]
                random_meals.append(random_meal)
            else:
                break

    return render(request, 'dishes/dishes.html', {'categories': categories, 'selected_category': selected_category, 'random_meals': random_meals})

# Returns a detail page for a user created dish
def dishes_detail(request, dish_id):
    dish = Dish.objects.get(id=dish_id)
    comments = Comment.objects.filter(dish_id=dish_id)
    print(comments)
    return render(request, 'dishes/detail.html', {'dish': dish,'comments': comments})

# Returns a page to view all dishes
@login_required
def dishes_index(request):
    dishes = Dish.objects.filter(user=request.user)
    return render(request, 'dishes/index.html', {'dishes': dishes})

# Create a dish w/ CBV
class DishCreate(LoginRequiredMixin, CreateView):
  model = Dish
  fields = ['name', 'origin', 'description']
  success_url = '/dishes/'
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

# Updates a dish w/ CBV
class DishUpdate(LoginRequiredMixin, UpdateView):
    model = Dish
    fields = ['origin', 'description']
    success_url = '/dishes'

# Deletes a dish w/ CBV
class DishDelete(LoginRequiredMixin, DeleteView):
    model = Dish
    success_url = '/dishes'

# Sign Up function
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

#Creates Comment
class CommentCreateView(CreateView):
    model = Comment
    fields = ['city_name', 'restaurant_name', 'body']

    def form_valid(self, form):
        dish = get_object_or_404(Dish, pk=self.kwargs['pk'])
        form.instance.dish_id = dish
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        dish_id = self.kwargs['pk']
        return reverse_lazy('detail', kwargs={'dish_id': dish_id})

# Updates Comments
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['city_name', 'restaurant_name', 'body']
<<<<<<< HEAD
    # success_url = reverse_lazy('detail')
    success_url = '/dishes'



  
=======
>>>>>>> main

    def form_valid(self, form):
        dish = get_object_or_404(Dish, pk=self.kwargs['pk'])
        form.instance.dish_id = dish
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        dish_id = self.kwargs['pk']
        return reverse_lazy('detail', kwargs={'dish_id': dish_id})

  
# Deletes comment
class CommentDeleteView(DeleteView):
    model = Comment
<<<<<<< HEAD
    success_url = reverse_lazy('detail')
=======

    def get_success_url(self):
        dish_id = self.object.dish_id.id
        return reverse_lazy('detail', kwargs={'dish_id': dish_id})


>>>>>>> main

# Returns all dishes in favorites
class MyListIndex(LoginRequiredMixin, ListView):
    model = MyList


<<<<<<< HEAD
# # Creates a dishes in favorites
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['city_name', 'restaurant_name', 'body']

    def get_success_url(self):
        dish_id = self.object.dish.id if self.object.dish else None
        return reverse_lazy('detail', kwargs={'dish_id': dish_id})    
=======
# # Creates a dish in favorites
class MyListCreate(LoginRequiredMixin, CreateView):
    model = MyList
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)     
>>>>>>> main


# Returns a Detail view on each dish
class MyListDetail(LoginRequiredMixin, DetailView):
    model = MyList

    def get_object(self, queryset=None):
        dish_id = self.kwargs.get('dish_id')
        mylist = get_object_or_404(MyList, dish__id=dish_id, user=self.request.user)
        return mylist


# Deletes a dish in favorites
class MyListDelete(LoginRequiredMixin, DeleteView):
    model = MyList
    success_url = '/mylist'


@login_required
def assoc_mylist(request, dish_id):
  MyList.objects.get(id=request.user.id).dish.add(dish_id)
  return redirect('mylist_index')

@login_required
def unassoc_mylist(request, dish_id, mylist_id):
  MyList.objects.get(id=mylist_id).dish.remove(dish_id)
  return redirect('mylist_index')

@login_required
def add_to_my_list(request, dish_name):
    if request.method == 'POST':
        user = request.user
        api_list, _ = APIList.objects.get_or_create(user=user)

        api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={dish_name}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            if data['meals']:
                dish = data['meals'][0]
                dish_name = dish['strMeal']
                dish_picture_url = dish['strMealThumb']

                apidish, created = APIDish.objects.get_or_create(name=dish_name, picture=dish_picture_url)

                api_list.dishes.add(apidish)
                return redirect('mylist_index')

    return redirect('daily_dish')

@login_required
def remove_from_my_list(request, dish_id):
    user = request.user
    api_list, created = APIList.objects.get_or_create(user=user)

    dish_to_remove = get_object_or_404(APIDish, id=dish_id)

    api_list.dishes.remove(dish_to_remove)
    return redirect('mylist_index')

@login_required
def mylist_index(request):
    mylist_exists = MyList.objects.filter(user=request.user).exists()
    if not mylist_exists:
        MyList.objects.create(user=request.user)
    mylist = MyList.objects.filter(user=request.user)

    user = request.user
    api_list, created = APIList.objects.get_or_create(user=user)

    favorite_dishes = api_list.dishes.all()

    return render(request, 'main_app/mylist_list.html', {'mylist': mylist, 'favorite_dishes': favorite_dishes})
