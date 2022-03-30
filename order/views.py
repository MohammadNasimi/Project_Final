from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, renderers
from rest_framework import permissions, generics
from django.utils import timezone

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


class Order_items_sessionDeleteView(View):
    def post(self, request, pk):
        from product.Cart import Cart
        cart = Cart(request)
        cart.remove(pk)
        response = render(request, 'landing/order/cart_list.html')
        response.set_cookie('count', len(cart))
        return response


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

    # def get(self, request):
    #     from core.models import User
    #     user = User.objects.get(id=request.session.get('uid'))
    #     from order.order_item_add import Order_User
    #     user = Order_User(user)
    #     print(user.get_user())
    #     order_id = user.get_user()[2]
    #     order_list = Order.objects.get(id=order_id)
    #     context = {
    #         'context': order_list
    #     }
    #     return render(request, 'landing/order/cart_list_order_customer.html', context=context)


class card_list_orderView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(address__customer__user_id=self.request.user.id, status_Order=1)

    renderer_classes = [renderers.JSONRenderer, renderers.TemplateHTMLRenderer]
    template_name = 'landing/order/cart_list_order_customer.html'


class order_items_update_Api(View):
    def post(self, request, pk):
        order_item_update = Order_item.objects.get(id=pk)
        order_item_update.Count = int(request.POST['number'])
        order_item_update.save()
        return render(request, 'landing/order/cart_list_order_customer.html')


class order_items_delete_Api(View):
    def post(self, request, pk):
        order_item_delete = Order_item.objects.get(id=pk)
        order_item_delete.delete()
        return render(request, 'landing/order/cart_list_order_customer.html')




class Order_delivery(View):
    def post(self, request, pk):
        now = timezone.now
        order_delivery = Order.objects.get(id=pk)
        print(order_delivery.status_Order)
        order_delivery.status_Order = 2
        # create_new_order = Order.objects.create(created=now, last_updated=now, is_deleted=0, is_active=1,
        #                                         status_Order=1, date=now,
        #                                         address=order_delivery.address.id,
        #                                         off_code=1)
        # create_new_order.save()
        order_delivery.save()
        return render(request, 'landing/order/cart_list_order_customer.html')


class Order_cancel(View):
    def post(self, request, pk):
        order_delivery = Order.objects.get(id=pk)
        print(order_delivery.status_Order)
        order_delivery.status_Order = 3
        order_delivery.save()
        return render(request, 'landing/order/cart_list_order_customer.html')
