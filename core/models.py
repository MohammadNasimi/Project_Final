from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from core.manager import BaseManager
from django.contrib.auth.models import AbstractUser, UserManager


class BaseModel(models.Model):
    """
        This model mixin usable for logical delete and logical activate status data.
    """
    created = models.DateTimeField(auto_now_add=True, editable=False, )
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    delete_timestamp = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(
        null=True, blank=True,
        verbose_name=_("Deleted Datetime"),
        help_text=_("This is deleted datetime")
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_("Deleted status"),
        help_text=_("This is deleted status")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Active status"),
        help_text=_("This is active status")
    )

    # custom manager for get active items
    objects = BaseManager()

    class Meta:
        abstract = True

    def deleter(self):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

    def activate(self):
        self.is_active = True
        self.save()


class BaseDiscount(BaseModel):
    value = models.PositiveIntegerField(null=False)
    type = models.CharField(max_length=10, choices=[('price', 'Price'), ('percent', 'Percent')], null=False)
    max_price = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    def profit_value(self, price: int):
        """
        Calculate and Return the profit of the discount
        :param price: int (item value)
        :return: profit
        """
        if self.type == 'price':
            return min(self.value, price)
        else:  # percent
            raw_profit = int((self.value / 100) * price)
            return int(min(raw_profit, int(self.max_price))) if self.max_price else raw_profit


class MyUserManager(UserManager):
    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    phone = models.CharField(max_length=20, null=True, blank=True, unique=True)
    USERNAME_FIELD = 'phone'
    objects = MyUserManager()
