from django.db import models
from core.models import BaseModel, BaseDiscount


# Create your models here.
class Discount(BaseDiscount):
    pass


class Category(BaseModel):
    category_name = models.CharField(max_length=20, null=True, blank=True)
    category_root = models.ForeignKey('self', on_delete=models.RESTRICT, null=False)
    discount = models.ForeignKey(Discount, on_delete=models.RESTRICT, null=False)


class Product(BaseModel):
    name_product = models.CharField(max_length=20, null=True, blank=True)
    brand = models.CharField(max_length=20, null=False)
    descriptions = models.TextField(max_length=250, null=False)
    price = models.PositiveIntegerField()
    number_store = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=15, choices=(('exist', True), ('Not exist', False)), default=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, null=True, blank=True)
    image = models.FileField(null=True, default='NO_pic.png', upload_to='Product_pic/%Y/%m/%d', blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.RESTRICT, null=False)
