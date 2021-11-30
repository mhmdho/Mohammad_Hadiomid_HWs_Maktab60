from django.contrib.auth import get_user_model
from rest_framework import serializers

from order.models import Order, OrderItem, EmailToCustomer, EmailToSupplier


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.Serializer):
    customer = UserSerializer()
    order_item = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = '__all__'

class EmailToCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailToCustomer
        fields = ['id', 'text', 'order_item']


class EmailToSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailToSupplier
        fields = ['id', 'text', 'order_item']










# class CategoryDetailSerializer(serializers.ModelSerializer):
#     posts = PostSerializer(source='category_posts', many=True)

