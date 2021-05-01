import copy

default_owner = {'first_name': '마틴', 'last_name': '파울러'}


def get_default_owner():
    return Person(default_owner)


def set_default_owner(arg):
    default_owner = arg


class Person:
    def __init__(self, data):
        self._last_name = data['last_name']
        self._first_name = data['first_name']

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, arg):
        self._last_name = arg

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, arg):
        self._first_name = arg
