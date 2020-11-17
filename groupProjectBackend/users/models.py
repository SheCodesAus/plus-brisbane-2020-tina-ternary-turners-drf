from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.TextField(max_length=30, blank=True)
    last_name = models.TextField(max_length=30, blank=True)
    email = models.TextField(max_length=30, blank=True)
    password = models.CharField(max_length=30)
   
    
    def __str__(self):
        return self.username
