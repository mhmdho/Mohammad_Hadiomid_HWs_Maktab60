from django.db import models
from myuser.models import Supplier
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    qty = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name





