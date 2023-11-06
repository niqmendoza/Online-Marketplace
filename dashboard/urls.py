from django.urls import path
from . import views

app_name = 'dashboard' #declaro nombre de app para que no conflicte con alguna otra cosa

urlpatterns = [
    path('', views.index, name='index'), #''= va a root, views.index= declaro cual es la view, name='index' ayuda a enrutar en el html despues
]