from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personalcode = models.CharField(max_length=6)
    status = models.CharField(max_length=6, default='출근')

# Create your models here.
