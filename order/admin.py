from django.contrib import admin
from order.models import Order_item, Of_code, Order


# Register your models here.
class Of_codeAdmin(admin.ModelAdmin):
    fields = ['value', 'type', 'max_price', 'off_code']
    list_display = ['value', 'type']
    list_filter = ['value', 'type']
    search_fields = ['value', 'type', 'off_code']


class Order_itemAdmin(admin.ModelAdmin):
    fields = ['Product', 'Count']
    list_display = ['Product']
    list_filter = ['Product', 'Count']
    search_fields = ['Product', 'Count']


class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General',
         {'fields': ['address', 'status_Order', 'date']}),
        ('order items', {'fields': ['order_items']}),
        ('off_code', {'fields': ['off_code']})
    )
    list_filter = ['address', 'date']
    search_fields = ['address', 'date', 'price']


admin.site.register(Of_code, Of_codeAdmin)
admin.site.register(Order_item, Order_itemAdmin)
admin.site.register(Order, OrderAdmin)
