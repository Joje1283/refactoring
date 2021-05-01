from playground import get_default_owner, set_default_owner

if __name__ == '__main__':
    owner1 = get_default_owner()
    assert "파울러" == owner1['last_name']

    owner2 = get_default_owner()
    owner2['last_name'] = '파슨스'
    assert "파슨스" == owner1['last_name']
