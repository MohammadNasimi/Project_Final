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
    def post(self, request, pk):
        delete_order_item = Order_item.objects.get(id=pk)
        delete_order_item.delete()
        return render(request, 'landing/order/cart_list.html')


class Order_items_sessionDeleteView(View):
    def post(self, request, pk):
        from product.Cart import Cart
        cart = Cart(request)
        cart.remove(pk)
        response = render(request, 'landing/order/cart_list.html')
        response.set_cookie('count', len(cart))
        return response


class Order_itemsUpdateView(View):
    def post(self, request, pk):
        order_item_get = Order_item.objects.get(id=pk)
        order_item_get.Count = int(request.POST['number'])
        order_item_get.save()
        return render(request, 'landing/public/profile.html')


class Order_itemsUpdate_sessionView(View):
    def post(self, request, pk):
        from product.Cart import Cart
        cart = Cart(request)
        cart.update(pk, int(request.POST['number']))
        response = render(request, 'landing/order/cart_list.html')
        response.set_cookie('count', len(cart))
        return response


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


class card_list_orderView(View):
    def get(self, request):
        return render(request, 'landing/order/cart_list_order_customer.html')
