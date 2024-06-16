from store.models import Product
from decimal import Decimal


class Basket():
    #basket class providing behaviours that can be inerited or overriden as necessary
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        product_id = str(product.id)

        #user cannot add multiple items more than the quantity shown
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product
        #select individual values inside of this data
        for item in basket.values():
            #translate price to deciamal so we can calculate total
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        #get the basket data and count qty
        #add items if exists
        return sum(item['qty'] for item in self.basket.values())

    def get_subtotal_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def get_total_price(self):

        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(11.50)

        total = subtotal + Decimal(shipping)
        return total
    def delete(self,product):
        #delete  item from session
        product_id=str(product)
        print(product_id)
        if product_id in self.basket:
            del self.basket[product_id]
        self.save()
    def update(self, product, qty):
        #update values of session
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()
    def save(self):
        self.session.modified = True