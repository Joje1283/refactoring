def in_new_england(customer):
    return customer['address']['state'] in ["MA", "CT", "ME", "VT", "NH", "RI"]


if __name__ == '__main__':
    some_customers = [
        {'address': {'state': 'MA'}},
        {'address': {'state': 'KO'}},
        {'address': {'state': 'AA'}},
    ]
    new_englanders = filter(lambda x: in_new_england(x), some_customers)
    print(list(new_englanders))
