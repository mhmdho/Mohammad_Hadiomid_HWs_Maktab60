from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import BooleanField

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


class AvailableProduct(models.Manager):
    def get_queryset(self):
        return super(AvailableProduct, self).get_queryset().filter(status=True)

class UnavailableProduct(models.Manager):
    def get_queryset(self):
        return super(UnavailableProduct, self).get_queryset().filter(status=False)

class Product(models.Model):
    name = models.CharField(max_length=200)
    buy_price = models.FloatField()
    sell_price = models.FloatField()
    qty = models.IntegerField()
    supplier = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    status = BooleanField(default=True)
    objects = models.Manager()
    available = AvailableProduct()
    unavailable = UnavailableProduct()

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name



