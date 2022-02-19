from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from core.models import BaseModel, User


class Address(BaseModel):
    province = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=False)
    town = models.CharField(max_length=20, null=False)
    street = models.CharField(max_length=20, null=False)
    alley = models.CharField(max_length=20, null=False)
    Plaque = models.IntegerField(unique=True, null=False)
    zip_code = models.IntegerField(unique=True, null=False)
    customer = models.ForeignKey('Customer', on_delete=models.RESTRICT)

    def __str__(self):
        return f'{self.city}:{self.zip_code}'

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')


class Customer(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')