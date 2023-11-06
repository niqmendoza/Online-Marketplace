from django.urls import path
from . import views

app_name= 'item'

urlpatterns = [
    path('', views.items, name='items'), #import la busqueda de items
    path('new/', views.new, name='new'), #importo el path de new(donde agregan items los usuarios *form.html*)
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'), #importo el delete
    path('<int:pk>/edit/', views.edit, name='edit'), #importo el edit
]