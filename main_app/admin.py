from django.contrib import admin
from .models import Dish, Comment, MyList, Photo


# Register your models here.
admin.site.register(Dish)
admin.site.register(Comment)
admin.site.register(MyList)
admin.site.register(Photo)

