from django.contrib import admin
from customer.models import Address, Customer


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    fields = ['province', 'city', 'town', 'street', 'alley', 'Plaque', 'zip_code', 'customer']
    list_display = ['province', 'city', 'town']
    list_filter = ['province', 'city', 'town']
    search_fields = ['province', 'city', 'town', 'zip_code', 'customer']


class CustomerAdmin(admin.ModelAdmin):
    fields = ['user']
    list_filter = ['user']
    search_fields = ['user']


admin.site.register(Address, AddressAdmin)
admin.site.register(Customer, CustomerAdmin)
