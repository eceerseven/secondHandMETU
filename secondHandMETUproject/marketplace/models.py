#marketplace/models.py
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='', null=True, blank=True)
    #email = models.EmailField(null=True, blank=True)
    #phone_number = models.CharField(max_length=15, null=True, blank=True)

def __str__(self):
    return self.item_name
    def __str__(self):
        return self.item_name
