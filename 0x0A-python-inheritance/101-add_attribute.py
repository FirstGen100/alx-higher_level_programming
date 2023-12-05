#!/usr/bin/python3
'''function to add attributes'''


def add_attribute(obj, attr_name, attr_value):
    '''function to add attribtes'''
    if hasattr(obj, 'attr_name'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
