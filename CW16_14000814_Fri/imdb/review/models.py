from typing import MappingView
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE
from ..movie.models import Movie
from django.contrib.auth import get_user_model
# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    rate = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_time = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    writer = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    class Meta:
        unique_together = [['movie', 'writer']]
     
    def __str__(self):
        return f"{self.movie} {self.writer}"