from django.shortcuts import render
from django.views import View
from django.views.generic import DeleteView
from rest_framework import viewsets, renderers
from rest_framework import permissions

# Create your views here.
from order.models import Order, Order_item
from order.serializers import OrderSerializer, Order_itemSerializer

from customer.permissions import IsOwnerPermission, IsSuperuserPermission


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = [IsOwnerPermission, permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(address__customer__user=self.request.user)

    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = 'landing/order/order_customer.html'


class Order_itemViewSets(viewsets.ModelViewSet):
    queryset = Order_item.objects.all()
    serializer_class = Order_itemSerializer


class Order_itemsDeleteView(View):
    def get(self, request, pk):
        delete_order_item = Order_item.objects.get(id=pk)
        delete_order_item.delete()
        return render(request, 'landing/public/profile.html')


class card_list(View):
    def get(self, request):
        from product.Cart import Cart
        cart = Cart(request)
        context = {
            'data_cart': cart.data_cart(),
            'data_product': cart.data_product(),
            'get_total_price': cart.get_total_price(),
            'len_cart': len(cart),

        }
        return render(request, 'landing/order/cart_list.html', context=context)
