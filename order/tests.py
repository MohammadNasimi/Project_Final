from django.test import TestCase
from product.models import Discount, Product, Category
from order.models import Order_item, Order, Of_code
from customer.models import Customer,Address


# Create your tests here.
class OrderTestcase(TestCase):
    def setUp(self):
        # create model for product
        self.discount1 = Discount.objects.create(value=20, type='percent', max_price='50000')
        self.discount2 = Discount.objects.create(value=2000, type='price')
        self.discount3 = Discount.objects.create(value=1500000, type='price')
        self.discount4 = Discount.objects.create(value=0, type='price')
        self.category1 = Category.objects.create(category_name='Food')
        self.category2 = Category.objects.create(category_name='Car', discount=self.discount1)
        self.category3 = Category.objects.create(category_name='Pizza', category_root=self.category1,
                                                 discount=self.discount2)
        self.product1 = Product.objects.create(name_product='Pizza peperoni', brand='Italy',
                                               descriptions='great pizza in Italy', price=30000, status=True,
                                               number_store=10,
                                               category=self.category3, discount=self.discount1)
        self.product2 = Product.objects.create(name_product='Samand', brand='Iran',
                                               descriptions='Made in Iran', price=230000000, status=True,
                                               number_store=2,
                                               category=self.category2, discount=self.discount3)
        self.product3 = Product.objects.create(name_product='perayd', brand='Iran',
                                               descriptions='Made in Iran', price=160000000, status=True,
                                               number_store=2,
                                               category=self.category2, discount=self.discount4)
        # create model of order_items
        self.order_item1 = Order_item.objects.create(Product=self.product1, Count=10)
        self.order_item2 = Order_item.objects.create(Product=self.product2, Count=1)
        self.order_item3 = Order_item.objects.create(Product=self.product3, Count=2)
        # create model of customer
        self.customer1 = Customer.objects.create(username='09142153654', password='123456')
        self.address1 = Address.objects.create(province='ahmad20', customer=self.customer1)
        # create model of Of_code
        self.off_code1 = Of_code.objects.create(value=0, type='price', off_code='123456')
        # create model of Order
        self.Order1 = Order.objects.create(customer=self.address1, off_code=self.off_code1)
        self.Order1.order_items.add(self.order_item1, self.order_item2, self.order_item3)
        self.Order1.save()
        self.Order2 = Order.objects.create(customer=self.address1, off_code=self.off_code1)
        self.Order2.order_items.add(self.order_item2, self.order_item3)
        self.Order2.save()

    def test_get_cost_end_product(self):
        self.assertEqual(self.order_item1.get_cost_end_product, 220000)
        self.assertEqual(self.order_item2.get_cost_end_product, 228450000)
        self.assertEqual(self.order_item3.get_cost_end_product, 319900000)

    def test_get_total_cost(self):
        # print(self.Order1.order_items.all())
        # print(self.Order2.order_items.all())
        # print(self.Order2.get_all_order_items)
        # print(self.Order2.objects.filter(order_items__Count=10))
        self.assertEqual(self.Order1.get_total_cost, 548570000)
        self.assertEqual(self.Order2.get_total_cost, 548350000)

    def test_get_all_order_items(self):
        self.assertEqual(self.Order1.get_all_order_items, ['Pizza peperoni', 'Samand', 'perayd'])
        self.assertEqual(self.Order2.get_all_order_items, ['Samand', 'perayd'])
