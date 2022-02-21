from django.db import models
from core.models import BaseModel, BaseDiscount
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Discount(BaseDiscount):
    pass

    def __str__(self):
        return f'{self.type}:{self.value}'

    class Meta:
        verbose_name = _('Discount')
        verbose_name_plural = _('Discounts')


class Category(BaseModel):
    category_name = models.CharField(max_length=20, null=True, blank=True)
    category_root = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories',
                                      verbose_name='Parent Category',
                                      null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category')


class Product(BaseModel):
    name_product = models.CharField(max_length=20, null=False)
    brand = models.CharField(max_length=20, null=True, blank=True)
    descriptions = models.TextField(max_length=250, null=True, blank=True)
    price = models.PositiveIntegerField(null=False)
    number_store = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=15, choices=(('exist', True), ('Not exist', False)), default=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, null=False)
    image = models.FileField(default='NO_pic.png', upload_to='Product_pic/%Y/%m/%d')
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name_product}'

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
