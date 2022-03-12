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
                            'order_items__Product_id', 'order_items__Count')  # get list order_item id
                        Order_item_user_product_id = Order.objects.filter(address_id=i, status_Order=1).values_list(
                            'order_items',
                            flat=True)
                        Order_id = Order.objects.filter(address_id=i, status_Order=1).values_list('id',
                                                                                                  flat=True).first()  # get list order_item id
                        if Order_item_user.exists() == True:
                            return Order_item_user, Address_Order, Order_id, len(
                                Order_item_user), Order_item_user_product_id
                        else:
                            Order_item_user = Order.objects.create(status_Order=1, off_code=1)
                            return Order_item_user

    def add_session(self, cart):
        data_session = cart.data_cart()
        product_exist_id = self.get_user()[0]
        Order_item_user_product_id = self.get_user()[4]
        dict_id_exist_product = {}
        for i in range(len(product_exist_id)):
            dict_id_exist_product[product_exist_id[i]['order_items__Product_id']] = Order_item_user_product_id[i]
        order_get_user_current = self.get_user()[2]
        order_user = Order.objects.get(id=order_get_user_current)
        for product_id, count in data_session.items():
            if int(product_id) in dict_id_exist_product.keys():

                order_exist =Order_item.objects.get(id=dict_id_exist_product[int(product_id)])
                order_exist.Count = order_exist.Count + int(count['count'])
                order_exist.save()
            else:
                product = Product.objects.get(id=product_id)
                order_item_new = Order_item.objects.create(Product=product, Count=int(count['count']))
                order_user.order_items.add(order_item_new)
                order_user.save()
