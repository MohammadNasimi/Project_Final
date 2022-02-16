from django.test import TestCase
from product.models import Discount, Product, Category


# Create your tests here.

class CategoryTestcase(TestCase):

    def setUp(self):
        self.discount1 = Discount.objects.create(value=20, type='percent', max_price='1000000')
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
                                               category=self.category2,discount=self.discount4)

    def test_profit_value(self):
        self.assertEqual(self.discount1.profit_value(10000), 2000)
        self.assertEqual(self.discount2.profit_value(10000), 2000)
        self.assertEqual(self.discount3.profit_value(10000), 10000)
        self.assertEqual(self.product1.discount.profit_value(30000), 6000)
        self.assertEqual(self.product2.discount.profit_value(230000000), 1500000)
        self.assertEqual(self.product3.category.discount.profit_value(160000000), 1000000)
