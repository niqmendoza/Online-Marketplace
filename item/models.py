from django.db import models
from django.contrib.auth.models import User #importo el User
#Creo el modelo de Category
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    #Hago que muestre el item como categories y no como categorys (django coloca una s al final de todo)
    class Meta:
        ordering = ('name',) #ordeno por nombre
        verbose_name_plural = 'Categories'

    #hago que muestre el nombre real y no 'Category object'   
    def __str__(self):
        return self.name
    
#Creo la tabla Item
class Item(models.Model):
    #categoria, la defino como Foreing y la vinculo con Category de arriba
    #esto con CASCADE hace que si borro una categoria todos los items de esa categoria se borran con el
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    
    #nombre del item
    name = models.CharField(max_length=255) 
    
    #descipcion del item, blank True y null=True para que permita dejar en blanco la desc
    description = models.TextField(blank=True, null=True) 
    
    #precio en formato float
    price = models.FloatField()
    
    #field para la imagen, upload_to='item_images' hace que se suba la imagen por un upload
    #si django no encuentra esta carpeta la crea
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    
    #se vendio?
    is_sold = models.BooleanField(default=False)
    
    #creado por, aca si el User es borrado entonces hace un CASCADE y borra todos los items que creo
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    
    #creado el dia
    created_at = models.DateTimeField(auto_now_add=True)
    
    #hago que muestre el nombre real y no 'item object'   
    def __str__(self):
        return self.name