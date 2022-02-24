from rest_framework import serializers

from order.models import Order, Order_item


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class Order_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_item
        fields = '__all__'
