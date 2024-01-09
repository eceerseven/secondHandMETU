# userAuthentication/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'email']


class ItemSearchForm(forms.Form):
    query = forms.CharField(label='Search for items', max_length=100)