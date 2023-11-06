from django.contrib import admin

# Register your models here.
from .models import Category, Item #importo el modelo de Category y Item

admin.site.register(Category) #lo registro dentro del admin center
admin.site.register(Item) #registro Item