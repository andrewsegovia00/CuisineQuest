from django import forms
from django.forms import ModelForm
from .models import Comment



class CommentForm(ModelForm):    
  class Meta:  
    model = Comment        
    fields = ('city_name', 'restaurant_name', 'body')


   