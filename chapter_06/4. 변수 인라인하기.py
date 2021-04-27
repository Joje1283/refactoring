# before
def func1(order):
    base_price = order['base_price']
    return base_price > 1000


# after
def func2(order):
    return order['base_price'] > 1000
