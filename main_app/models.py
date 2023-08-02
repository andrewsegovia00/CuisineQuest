from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

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