from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.views import OrderViewSets, Order_itemViewSets, card_list, \
    Order_items_sessionDeleteView, Order_itemsUpdate_sessionView, card_list_orderView, order_items_update_Api, \
    order_items_delete_Api, Order_delivery, Order_cancel

router = DefaultRouter()
router.register('Order', OrderViewSets, basename='Order')
router.register('Order_item', Order_itemViewSets, basename='Order_item')
app_name = 'order'
urlpatterns = [
    path('', include(router.urls)),
    path('delete_order_item/<int:pk>', order_items_delete_Api.as_view(), name='delete_order_item'),
    path('delete_order_item_session/<int:pk>', Order_items_sessionDeleteView.as_view(),
         name='delete_order_item_session'),
    path('update_order_item/<int:pk>', order_items_update_Api.as_view(), name='update_order_item'),
    path('update_order_item_session/<int:pk>', Order_itemsUpdate_sessionView.as_view(),
         name='update_order_item_session'),
    path('card_list/', card_list.as_view(), name='card_list'),
    path('card_list_order/', card_list_orderView.as_view(), name='card_list_order'),
    path('Order_delivery/<int:pk>', Order_delivery.as_view(), name='Order_delivery'),
    path('Order_cancel/<int:pk>', Order_cancel.as_view(), name='Order_cancel'),
]
