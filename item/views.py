from django.shortcuts import render, get_object_or_404, redirect #importo get_object_or_404 
from django.contrib.auth.decorators import login_required #importo un decorador de django
from django.db.models import Q

from .forms import NewItemForm, EditItemForm#importo el NewItemForm que cree en forms.py de Item
from .models import Category, Item #importo el modelo de Item

#Busqueda de items
def items(request):
    query = request.GET.get('query','') #para el {{query}} de items.html
    category_id = request.GET.get('category', 0) #category id
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    
    if category_id:
        items = items.filter(category_id=category_id)
    
    #hago un loop para la busqueda
    if query: #si el usuario busca algo 
        items = items.filter(Q(name__icontains=query) |Q(description__icontains=query))#esto es como una query de sql LIKE, tipo "SELECT ... WHERE headline ILIKE '%Lennon%';"

    return render(request, 'item/items.html', {
        'items':items,
        'query':query, #paso al front el query
        'categories':categories,
        'category_id': int(category_id), #converti a int sino no funciona la busqueda
    })
#Detail Page
def detail(request, pk):
    item= get_object_or_404(Item, pk=pk)
#-variable       -filtro       -traigo solo los items de esa categoria en la que esta  -exluyo este item -traigo solo 3 resultados
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    
    return render(request, 'item/detail.html',{
        'item':item,
        'related_items':related_items #traigo related items creado arriba
    })

#view del form
@login_required #decorador
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False) #si se guardase ahora no tendria el created_by y tiraria error por eso el commit=false
            item.created_by = request.user #siempre estaria el usuario gracias al decorador de login_requered
            item.save()
            
            return redirect('item:detail', pk=item.id)
        else:
            form = NewItemForm()
        
    form = NewItemForm()
    
    return render(request, 'item/form.html', {
        'form': form,
        'title':'Item nuevo',
    })
#view del edit item
@login_required #decorador
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            
            return redirect('item:detail', pk=item.id)
        else:
            form = EditItemForm(instance=item)
        
    form = EditItemForm()
    
    return render(request, 'item/form.html', {
        'form': form,
        'title':'Editar Item',
    })
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')