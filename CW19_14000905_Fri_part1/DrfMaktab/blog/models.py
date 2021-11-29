from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
