from django.db import models
from core.models import BaseModel, BaseDiscount
from product.models import Product


# Create your models here.


class Of_code(BaseDiscount):
    off_code = models.CharField(max_length=10, unique=True)



