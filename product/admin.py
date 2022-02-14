from django.contrib import admin
from product.models import Discount, Category, Product

# Register your models here.
admin.site.register(Discount)
admin.site.register(Category)
admin.site.register(Product)
