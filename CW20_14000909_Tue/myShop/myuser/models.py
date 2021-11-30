from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model


# Create your models here.


class Favorite(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    customer = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.customer} saved {self.product}"


class Comment(models.Model):
    description = models.CharField(max_length=400)
    customer = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    product = models.ForeignKey('product.Product', on_delete=CASCADE)

    def __str__(self):
        return f"{self.customer} commented {self.product}"


