from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.views import OrderViewSets, Order_itemViewSets,Order_itemsDeleteView,card_list

router = DefaultRouter()
router.register('Order', OrderViewSets, basename='Order')
router.register('Order_item', Order_itemViewSets, basename='Order_item')
app_name = 'order'
urlpatterns = [
    path('', include(router.urls)),
    path('delete_order_item/<int:pk>', Order_itemsDeleteView.as_view(),name='delete_order_item'),
    path('card_list/', card_list.as_view(), name='card_list'),
]
