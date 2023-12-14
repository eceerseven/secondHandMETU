#userAuthentication/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    website = models.URLField(blank=True)
    #some of the files did not used at this stage
    # but implemented for next stage of the project for example user website/bio.

    def __str__(self):
        return self.user.username
