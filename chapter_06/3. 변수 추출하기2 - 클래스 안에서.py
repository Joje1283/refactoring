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
        return self.quantity * self.item_price - \
               max(0, self.quantity - 500) * self.item_price * 0.05 + \
               min(self.quantity * self.item_price * 0.1, 100)


if __name__ == '__main__':
    order = Order({
        'quantity': 10,
        'item_price': 1000,
    })
    print(order.price)
