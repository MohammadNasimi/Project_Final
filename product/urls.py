from django.urls import path

from .views import CategoryListview

app_name = 'product'
urlpatterns = [
    path('Category/', CategoryListview.as_view(), name='category'),
]
