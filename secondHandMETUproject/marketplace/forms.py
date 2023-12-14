# marketplace/forms.py
from django import forms
from .models import Item


class SellItemForm(forms.ModelForm):
    CONDITION_CHOICES = [
        ('lightly_used', 'Lightly Used'),
        ('moderately_used', 'Moderately Used'),
        ('heavily_used', 'Heavily Used'),
        ('like_new', 'Like New'),
        ('brand_new', 'Brand New'),
    ]
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('furniture', 'Furniture'),
        ('books', 'Books'),
        ('toys', 'Toys'),
        ('sports', 'Sports Equipment'),
        ('music_instruments', 'Musical Instruments'),
        ('jewelry', 'Jewelry'),
        ('automotive', 'Automotive'),
        ('other', 'Other'),
    ]


    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    condition = forms.ChoiceField(choices=CONDITION_CHOICES)

    image = forms.ImageField()

    class Meta:
        model = Item
        exclude = ['user']

