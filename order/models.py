from django.db import models
from core.models import BaseModel, BaseDiscount
from product.models import Product


# Create your models here.


class Of_code(BaseDiscount):
    off_code = models.CharField(max_length=10, unique=True)


class Order_items(BaseModel):
    Product = models.ForeignKey(Product, on_delete=models.RESTRICT, null=True, blank=True)
    Count = models.PositiveIntegerField(null=True, blank=True, default=1)
    Price_product = models.PositiveIntegerField(null=True, default=0)
