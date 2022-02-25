from rest_framework import serializers

from customer.serializers import AddressSerializer
from product.serializers import ProductSerializer
from order.models import Order, Order_item


class Order_itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_item
        fields = '__all__'

    Product = ProductSerializer(read_only=True)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    address = AddressSerializer(read_only=True)
    # order_item_set = serializers.HyperlinkedRelatedField(view_name='order:Order_item',
    #                                                       queryset=Order_item.objects.all(), many=True)
