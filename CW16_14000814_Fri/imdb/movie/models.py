from django.db import models
from genre.models import Genre

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=72)
    director = models.CharField(max_length=72)
    genre = models.ManyToManyField('genre')
    created_date = models.DateField(max_length=4)
    long = models.PositiveIntegerField()
    summery = models.TextField()

    def __str__(self):
        return f"{self.name} {self.created_date}"

# class Genre(models.Model):
#     name = models.CharField(max)