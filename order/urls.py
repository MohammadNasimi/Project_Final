from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.views import OrderViewSets,Order_itemViewSets

router = DefaultRouter()
router.register('Order', OrderViewSets, basename='Order')
router.register('Order_item', Order_itemViewSets, basename='Order_item')
app_name = 'order'
urlpatterns = [
    path('', include(router.urls)),
]
