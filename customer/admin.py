from django.contrib import admin
from customer.models import Address, Customer


# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    fields = ['province', 'city', 'town', 'street', 'alley', 'Plaque', 'zip_code']
    list_display = ['province', 'city', 'town']
    list_filter = ['province', 'city', 'town']
    search_fields = ['province', 'city', 'town', 'zip_code']


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Address, AddressAdmin)
admin.site.register(Customer, CustomerAdmin)
