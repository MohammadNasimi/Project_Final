from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from core.models import BaseModel


class Address(BaseModel):
    province = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=20, null=False)
    town = models.CharField(max_length=20, null=False)
    street = models.CharField(max_length=20, null=False)
    alley = models.CharField(max_length=20, null=False)
    Plaque = models.IntegerField(unique=True, null=False)
    zip_code = models.IntegerField(unique=True, null=False)

    def __str__(self):
        return f'{self.city}:{self.zip_code}'


class Customer(User):
    pass
    # phone = models.CharField(max_length=20, null=True, blank=True)
    # address = models.ForeignKey(Address, on_delete=models.RESTRICT)
