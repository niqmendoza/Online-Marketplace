from django.shortcuts import render,redirect

#importo los modelos
from item.models import Category, Item

#importo la autenticacion de usuario de forms.py
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6] #para que solo muestre los items no vendidos
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories':categories,
        'items':items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request): #vista de signup
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        
    else:
        form = SignupForm()   
    
    form = SignupForm()
    
    return render(request, 'core/signup.html', { 
        'form':form
    } )
