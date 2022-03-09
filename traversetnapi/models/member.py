from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(
        max_length=150,
        default='none'
    )
    name = models.CharField(
        max_length=50,
        default='none'
    )
    