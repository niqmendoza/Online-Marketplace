from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #importo auth de django
from django.contrib.auth.models import User

#login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username', #placeholder
        'class': 'w-full py-4 px-6 rounded-xl', #con class puedo editar el css con tailwind
        
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password', #placeholder
        'class': 'w-full py-4 px-6 rounded-xl', #con class puedo editar el css con tailwind
        
    }))
    

#signup
class SignupForm(UserCreationForm):
    class Meta:
        model = User #importo el modelo de User
        fields = ('username','email','password1','password2') #le digo que campos debe utilizar
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username', #placeholder
        'class': 'w-full py-4 px-6 rounded-xl', #con class puedo editar el css con tailwind
        
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email', #placeholder
        'class': 'w-full py-4 px-6 rounded-xl', #con class puedo editar el css con tailwind
        
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password', #placeholder
        'class': 'w-full py-4 px-6 rounded-xl', #con class puedo editar el css con tailwind
        
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password', #placeholder
        'class': 'w-full py-4 px-6 rounded-xl', #con class puedo editar el css con tailwind
        
    }))