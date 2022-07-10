from argparse import _MutuallyExclusiveGroup
from django.utils import timezone
from platform import release
from turtle import title
from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE, related_name="genre")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
