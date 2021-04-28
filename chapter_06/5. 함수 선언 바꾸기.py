def in_new_england(customer):
    state_code = customer['address']['state']
    return state_code in ["MA", "CT", "ME", "VT", "NH", "RI"]


if __name__ == '__main__':
    some_customers = [
        {'address': {'state': 'MA'}},
        {'address': {'state': 'KO'}},
        {'address': {'state': 'AA'}},
    ]
    new_englanders = filter(lambda x: in_new_england(x), some_customers)
    print(list(new_englanders))
