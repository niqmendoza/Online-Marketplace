from django.contrib.auth import views as auth_views #lo importo con un as para que no conflicte con el de abajo
from django.urls import path

from . import views
from .forms import LoginForm #importo el LoginForm

app_name='core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'), #contact.html
    path('signup/', views.signup, name='signup'), #signup
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login') #login
]
