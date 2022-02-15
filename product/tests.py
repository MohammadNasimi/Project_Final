from django.test import TestCase
from product.models import Discount, Product, Category


# Create your tests here.

class CategoryTestcase(TestCase):

    def setUp(self):
        self.discount1 = Discount.objects.create(value=20, type='percent', max_price='10000')
        self.discount2 = Discount.objects.create(value=2000, type='Price', max_price='10000')
        self.category1 = Category.objects.create(category_name='Food')
        self.category2 = Category.objects.create(category_name='Car', discount=self.discount1)
        self.category2 = Category.objects.create(category_name='Pizza', category_root=self.category1,
                                                 discount=self.discount1)
        self.product = Product.objects.create(name_product='Pizza peperoni', brand='Italy',
                                              descriptions='great pizza in Italy', price=30000, status=True,
                                              category=self.category2)
    