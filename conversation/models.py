from django.contrib.auth.models import User
from django.db import models

from item.models import Item #import el modelo de Item


class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE) #relaciono con una foreign key al modelo de Item
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-modified_at',)
        
class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages',on_delete=models.CASCADE)