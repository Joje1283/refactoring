class Order:
    def __init__(self, record):
        self._data = record

    @property
    def quantity(self):
        return self._data['quantity']

    @property
    def item_price(self):
        return self._data['item_price']

    @property
    def price(self):
        return self.base_price - self.quantity_discount + self.shipping

    @property
    def base_price(self):
        return self.quantity * self.item_price

    @property
    def quantity_discount(self):
        return max(0, self.quantity - 500) * self.item_price * 0.05

    @property
    def shipping(self):
        return min(self.base_price * 0.1, 100)


if __name__ == '__main__':
    order = Order({
        'quantity': 10,
        'item_price': 1000,
    })
    print(order.price)
