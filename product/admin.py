from django.contrib import admin
from product.models import Discount, Category, Product
from django.contrib import admin


# Register your models here.
class DiscountAdmin(admin.ModelAdmin):
    fields = ['value', 'type', 'max_price']
    list_display = ['value', 'type']
    list_filter = ['value', 'type']
    search_fields = ['value', 'type']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_name', 'category_root', 'discount']
    list_display = ['category_name']
    list_filter = ['category_name', 'discount']
    search_fields = ['category_name', 'category_root']


class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('General',
         {'fields': ['name_product', 'brand', 'descriptions']}),
        ('Info', {'fields': ['price', 'number_store', 'category', 'status', 'discount']}),
        ('Image', {'fields': ['image']})
    )
    list_filter = ['name_product', 'category']
    search_fields = ['name_product', 'brand', 'price']


admin.site.register(Discount, DiscountAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
