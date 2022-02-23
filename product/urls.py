from django.urls import path

from .views import product_for_categoryListview

app_name = 'product'
urlpatterns = [
    # path('Category/', CategoryListview.as_view(), name='category'),
    # path('product/', productListview.as_view(), name='product'),
    path('category_product/<int:pk>', product_for_categoryListview.as_view(), name='category_product'),
]
