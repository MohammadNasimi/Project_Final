from django.test import TestCase
from product.models import Discount, Product, Category


# Create your tests here.

class CategoryTestcase(TestCase):

    def setUp(self):
        self.discount1 = Discount.objects.create(value=20, type='percent', max_price='10000')
        self.discount2 = Discount.objects.create(value=2000, type='price')
        self.discount3 = Discount.objects.create(value=15000, type='price')
        self.category1 = Category.objects.create(category_name='Food')
        self.category2 = Category.objects.create(category_name='Car', discount=self.discount1)
        self.category2 = Category.objects.create(category_name='Pizza', category_root=self.category1)
        self.product = Product.objects.create(name_product='Pizza peperoni', brand='Italy',
                                              descriptions='great pizza in Italy', price=30000, status=True,
                                              number_store=10,
                                              category=self.category2, discount=self.discount1)

    def test1_profit_price10000(self):
        self.assertEqual(self.discount1.profit_value(10000), 2000)
        self.assertEqual(self.discount2.profit_value(10000), 2000)
        self.assertEqual(self.discount3.profit_value(10000), 10000)
        self.assertEqual(self.product.discount.profit_value(30000), 6000)
