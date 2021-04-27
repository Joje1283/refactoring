def price(order):
    return order['quantity'] * order['item_price'] - \
           max(0, order['quantity'] - 500) * order['item_price'] * 0.05 + \
           min(order['quantity'] * order['item_price'] * 0.1, 100)


if __name__ == '__main__':
    print(price({
        'quantity': 10,
        'item_price': 1000,
    }))
