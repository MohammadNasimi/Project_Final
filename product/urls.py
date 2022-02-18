from django.urls import path

from .views import CategoryView

app_name = 'product'
urlpatterns = [
    path('Category/', CategoryView.as_view(), name='category'),
]
