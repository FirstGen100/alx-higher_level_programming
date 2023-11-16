#!/usr/bin/python3
'''function to add attributes'''


def add_attribute(obj, attr_name, attr_value):
    '''function to add attribtes'''
    if attr_name in obj.__dict__:
        raise TypeError("can't add new attribute")
    else:
        obj.__setattr__(attr_name, attr_value)
