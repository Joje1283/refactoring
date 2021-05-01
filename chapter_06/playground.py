import copy

default_owner = {'first_name': '마틴', 'last_name': '파울러'}


def get_default_owner():
    return copy.deepcopy(default_owner)


def set_default_owner(arg):
    default_owner = arg
