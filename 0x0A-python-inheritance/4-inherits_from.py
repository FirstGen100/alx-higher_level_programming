#!/usr/bin/python3
'''returns true if object is an isnstance of a class'''


def inherits_from(obj, a_class):
    '''returns true if object is an instance of a class'''

    return type(obj) != a_class and isinstance(obj, a_class)
