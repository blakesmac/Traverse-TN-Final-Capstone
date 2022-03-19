from django.db import models
from .member import Member

class Place(models.Model):
    address = models.CharField(
        max_length=50,
        default='none'
    )
    wildlife = models.CharField(
        max_length=100,
        default='none'
    )
    about = models.CharField(
        max_length=150,
        default='none'
    )
    visitors = models.ManyToManyField(
        Member,
        related_name="places",
    )