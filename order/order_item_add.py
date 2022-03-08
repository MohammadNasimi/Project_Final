from customer.models import Customer
from order.models import Order, Order_item
from customer.models import Address
from product.models import Product


class Order_User(object):
    def __init__(self, user):
        self.user = user

    def get_user(self):
        for user in Customer.objects.all():
            if user.user_id == self.user.id:
                address = Address.objects.filter(customer_id=user.id).values_list('id', flat=True).order_by('id')
                for i in address:
                    Address_Order = Order.objects.filter(address_id=i, status_Order=1).values_list('address',
                                                                                                   flat=True)  # get address id
                    if Address_Order:
                        Order_item_user = Order.objects.filter(address_id=i, status_Order=1).values_list('order_items',
                                                                                                         flat=True).values(
                            'order_items__Product_id')  # get list order_item id
                        Order_id = Order.objects.filter(address_id=i, status_Order=1).values_list('id',
                                                                                                  flat=True).first()  # get list order_item id
                        return Order_item_user, Address_Order, Order_id

    def add_session(self, cart):
        data_session = cart.data_cart()
        product_exist_id = self.get_user()
        order_get_user_current = self.get_user()[2]
        order_user = Order.objects.get(id=order_get_user_current)
        for product_id, count in data_session.items():
            product = Product.objects.get(id=product_id)
            order_item_new = Order_item.objects.create(Product=product, Count=count['count'])
            order_user.order_items.add(order_item_new)
            order_user.save()
