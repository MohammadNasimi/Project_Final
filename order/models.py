import datetime

from django.db import models
from core.models import BaseModel, BaseDiscount
from product.models import Product
from customer.models import Address

from model_utils import Choices

from django.utils import timezone

from django.utils.translation import gettext_lazy as _


# Create your models here.


class Of_code(BaseDiscount):
    off_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.type}:{self.value}'

    class Meta:
        verbose_name = _('Off_code')
        verbose_name_plural = _('Off_codes')


class Order_item(BaseModel):
    Product = models.ForeignKey(Product, on_delete=models.RESTRICT, null=False)
    Count = models.PositiveIntegerField(null=True, blank=True, default=1)

    def __str__(self):
        return f'{self.Product}:{self.Count}'

    @property
    def get_cost_end_product(self):
        return ((self.Product.price - self.Product.category.discount.profit_value(self.Product.price)) -
                self.Product.discount.profit_value(self.Product.price)) * self.Count

    class Meta:
        verbose_name = _('Order item')
        verbose_name_plural = _('Order items')


ORDER_STATUS = Choices(
    (1, 'Current', 'Current'),
    (2, 'Delivered', 'Delivered'),
    (3, 'Canceled', 'Canceled')
)


class Order(BaseModel):
    address = models.ForeignKey(Address, on_delete=models.RESTRICT, null=False)
    order_items = models.ManyToManyField(Order_item)
    status_Order = models.IntegerField(choices=ORDER_STATUS, default=1, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    off_code = models.ForeignKey(Of_code, on_delete=models.RESTRICT)

    @property
    def get_total_cost(self):
        return sum(item.get_cost_end_product for item in self.order_items.all())

    @property
    def get_all_order_items(self):
        return [item.Product.name_product for item in self.order_items.all()]

    def __str__(self):
        return f'{self.customer}:{self.date.year}'

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Order')
