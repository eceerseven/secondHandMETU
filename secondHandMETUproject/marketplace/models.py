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
    image = models.ImageField(upload_to='secondHandMETU\secondHandMETUproject\static\images', null=True, blank=True)


    def __str__(self):
        return self.item_name
