from django import forms

from .models import Item #importo el modelo de Item de los modelos

#creo una variable para los estilos, asi no tengo que repetir codigo de tailwind
INPUT_CLASSES = 'w-full py-4 py-6 rounded-xl border'

#creo un form para cargar el nuevo item
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item #declaro que el modelo sera el de Item que importe arriba
        fields = ('category', 'name', 'description', 'price', 'image',)
        
        #puedo agregar styling de esta forma
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
#creo un form para editar los items 
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item #declaro que el modelo sera el de Item que importe arriba
        fields = ( 'name', 'description', 'price', 'image', 'is_sold')
        
        #puedo agregar styling de esta forma
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }
        
        