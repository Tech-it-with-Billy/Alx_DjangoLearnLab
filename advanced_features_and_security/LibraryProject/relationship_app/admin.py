from django.contrib import admin
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_ofBirth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)