from django.db import models
from django.utils import timezone


class Genre(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=255)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    date_created = models.DateTimeField(
        default=timezone.now)  # Passed a reference
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
