from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=120)
    Email = models.EmailField()
    phone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=120)
    Email = models.EmailField()
    phone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.name


class Favorite(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.customer} saved {self.product}"


class Comment(models.Model):
    description = models.CharField(max_length=400)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=CASCADE)

    def __str__(self):
        return f"{self.customer} commented {self.product}"


