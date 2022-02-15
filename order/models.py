from django.db import models
from core.models import BaseModel, BaseDiscount
from product.models import Product
from customer.models import Customer

from model_utils import Choices


# Create your models here.


class Of_code(BaseDiscount):
    off_code = models.CharField(max_length=10, unique=True)


class Order_item(BaseModel):
    Product = models.ForeignKey(Product, on_delete=models.RESTRICT, null=False)
    Count = models.PositiveIntegerField(null=True, blank=True, default=1)
    Price_product = models.PositiveIntegerField(null=False, default=0)

    @property
    def get_cost_end_product(self):
        return ((self.Product.price - self.Product.category.discount.profit_value(self.Product.price)) -
                self.Product.discount.profit_value(self.Product.price)) * self.Count


ORDER_STATUS = Choices(
    (1, 'Current', 'Current'),
    (2, 'Delivered', 'Delivered'),
    (3, 'Canceled', 'Canceled')
)


class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT, null=False)
    order_items = models.ManyToManyField(Order_item)
    status_Order = models.IntegerField(choices=ORDER_STATUS, default=1, null=True, blank=True)
    date = models.DateTimeField()
    price_all = models.PositiveIntegerField()
    off_code = models.ForeignKey(Of_code, on_delete=models.RESTRICT)
