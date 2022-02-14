from django.db import models
from core.models import BaseModel, BaseDiscount
from product.models import Product
from customer.models import Customer


# Create your models here.


class Of_code(BaseDiscount):
    off_code = models.CharField(max_length=10, unique=True)


class Order_items(BaseModel):
    Product = models.ForeignKey(Product, on_delete=models.RESTRICT, null=True, blank=True)
    Count = models.PositiveIntegerField(null=True, blank=True, default=1)
    Price_product = models.PositiveIntegerField(null=True, default=0)


status = (('Current', 1), ('Delivered', 2), ('Canceled', 3))


class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, null=True, blank=True)
    order_items = models.ManyToManyField(Order_items, on_delete=models.RESTRICT, null=True, blank=True)
    status_Order = models.PositiveIntegerField(choices=status, default=1, null=True, blank=True)
    date = models.DateTimeField()
    price_all = models.PositiveIntegerField()
    off_code = models.ForeignKey(Of_code, on_delete=models.RESTRICT)