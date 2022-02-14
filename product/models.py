from django.db import models
from core.models import BaseModel, BaseDiscount


# Create your models here.
class Discount(BaseDiscount):
    pass

class Category(BaseModel):
    category_name = models.CharField(max_length=20, null=True, blank=True)
    category_root = models.ForeignKey('self', on_delete=models.RESTRICT, null=False)
    discount = models.ForeignKey(Discount, on_delete=models.RESTRICT, null=False)




