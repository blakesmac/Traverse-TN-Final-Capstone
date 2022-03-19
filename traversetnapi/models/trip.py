from django.db import models
from .place import Place
from .river import River
from .member import Member

class Trip(models.Model):
    title = models.CharField(max_length=50)
    river = models.ForeignKey(
        River,
        verbose_name="River",
        null=True,
        on_delete=models.SET_NULL
    )
    place = models.ForeignKey(
        Place,
        verbose_name="Place",
        null=True,
        on_delete=models.SET_NULL
    )
    date = models.DateField(auto_now_add=True)
    member = models.ForeignKey(
        Member,
        related_name="trips",
        null=True,
        on_delete=models.SET_NULL
    )