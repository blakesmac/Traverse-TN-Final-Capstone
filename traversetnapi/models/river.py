from django.db import models
from traversetnapi.models.member import Member

class River(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    fish = models.CharField(max_length=50)
    animals = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    flowchart = models.CharField(max_length=50)
    visitors = models.ForeignKey(
        Member,
        related_name="rivers",
        null=True,
        on_delete=models.CASCADE
    )