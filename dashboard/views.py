from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from item.models import Item #importo el modelo de Item

@login_required
def index(request):
    items = Item.objects.filter(created_by = request.user) #filtro de items por usuario que lo creo
    
    return render(request, 'dashboard/index.html', {
        'items':items,
    })
    

