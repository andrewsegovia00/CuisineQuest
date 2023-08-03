from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.full_name

# Dish Model
class Dish(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    picture = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'food_id': self.id})

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dish_id = models.ForeignKey(Dish,on_delete=models.CASCADE,related_name='comments')    
    city_name = models.CharField(max_length=80, verbose_name='City', default='')    
    restaurant_name = models.CharField(max_length=100, verbose_name='Restaurant Name', default='')
    body = models.TextField()    
    created_on = models.DateTimeField(auto_now_add=True)   
        
    class Meta:        
        ordering = ['created_on']    
    
    
    def __str__(self):        
        return 'Comment by {} on dish = {}'.format(self.user, self.dish_id)

# My List Model
class MyList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ManyToManyField(Dish)
    
    def __str__(self):
        return f"{self.user}'s List"
    
class APIDish(models.Model):
    name = models.CharField(max_length=255)
    picture = models.URLField()

    def __str__(self):
        return self.name
    def create_dish_instance(self):
        return Dish.objects.create(name=self.name, origin='Unknown', description='Unknown', picture='')
    
class APIList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(APIDish)

    def __str__(self):
        return f"{self.user}'s List"

class Photo(models.Model):
    url = models.CharField(max_length=200)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for dish_id: {self.dish_id} @{self.url}"
    