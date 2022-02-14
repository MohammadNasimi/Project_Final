from django.contrib import admin
from order.models import Order_item, Of_code, Order

# Register your models here.
admin.site.register(Of_code)
admin.site.register(Order_item)
admin.site.register(Order)
