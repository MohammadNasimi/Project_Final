from product.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('Cart_list')
        if not cart:
            cart = self.session['Cart_list'] = {}
        self.cart = cart

    def add(self, product_id, count):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'count': count, 'price': Product.objects.get(id=int(product_id)).price}
        else:
            count_per = int(self.cart[product_id]['count'])
            self.cart[product_id]['count'] = int(count) + count_per
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def update(self, product, new_count):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['count'] = new_count
            print(self.cart[product_id]['count'])
            print(new_count)
            self.save()
            print(self.cart[product_id]['count'])

    def data_product(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)  # < QuerySet [<Product: soda>, <Product: devo>]>
        return products

    def data_cart(self):
        cart = self.cart.copy()  # {'6': {'count': '1', 'price': 1000000}, '4': {'count': 10, 'price': 15000}}
        for item in cart.values():
            item['total_price'] = int(item['price']) * int(item['count'])
            self.save()
        cart = self.cart.copy()
        return cart

    def __len__(self):
        return sum(int(item['count']) for item in self.cart.values())

    def get_total_price(self):
        return sum(int(item['count']) * int(item['price']) for item in self.cart.values())

    def clear(self):
        del self.session['Cart_list']
