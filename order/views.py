from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from order.models import Order,Order_item
from order.serializers import OrderSerializer, Order_itemSerializer


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class Order_itemViewSets(viewsets.ModelViewSet):
    queryset = Order_item.objects.all()
    serializer_class = Order_itemSerializer
