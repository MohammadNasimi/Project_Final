from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from core.models import BaseModel


class Address(BaseModel):
    province = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    town = models.CharField(max_length=20, null=True, blank=True)
    street = models.CharField(max_length=20, null=True, blank=True)
    alley = models.CharField(max_length=20, null=True, blank=True)
    Plaque = models.IntegerField(unique=True, null=True, blank=True)
    zip_code = models.IntegerField(unique=True, null=True, blank=True)


class Customer(User):
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.RESTRICT)
