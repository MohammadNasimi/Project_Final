from django.test import TestCase
from product.models import Discount, Product, Category
from order.models import Order_item, Order, Of_code


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

    def test_get_cost_end_product(self):
        self.assertEqual(self.order_item1.get_cost_end_product, 220000)
        self.assertEqual(self.order_item2.get_cost_end_product, 228450000)
        self.assertEqual(self.order_item3.get_cost_end_product, 319900000)
