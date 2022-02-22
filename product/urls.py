from django.urls import path

from .views import CategoryListview, productListview

app_name = 'product'
urlpatterns = [
    path('Category/', CategoryListview.as_view(), name='category'),
    path('product/', productListview.as_view(), name='product'),
]
