from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    order_num = models.CharField(max_length=10)
    order_date = models.DateField()
    total_count = IntegerField()
    total_price = IntegerField()

    def __str__(self):
        return f"{self.customer} factor{self.order_num}"


class OrderItem(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.SET_NULL, null=True)
    unit_price=models.IntegerField()
    item_qty = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} from {self.order}"


class EmailToSupplier(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    delivery = models.BooleanField(default=True)

    def __str__(self):
        return f"Email to Supplier: {self.order_item}"


class EmailToCustomer(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    delivery = models.BooleanField(default=True)

    def __str__(self):
        return f"Email to Customer: {self.order}"
