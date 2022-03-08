from tkinter import CASCADE
from django.db import models
from .member import Member
from .river import River
from .place import Place


class Favorite(models.Model):
    riverId = models.ForeignKey(
        River,
        verbose_name="River",
        null=True,
        on_delete=models.CASCADE
    )
    placeId = models.ForeignKey(
        Place,
        verbose_name="Place",
        null=True,
        on_delete=models.SET_NULL
    )
    memberId = models.ForeignKey(
        Member,
        related_name="favorites",
        null=True,
        on_delete=models.SET_NULL
    )