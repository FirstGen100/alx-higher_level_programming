#!/usr/bin/python3
'''
    a function to add 2 integers
'''


def add_integer(a, b=98):
    '''function to add 2 ints'''
    if type(a) == float or type(a) == int:
        a = int(a)
    else:
        raise TypeError('a must be an integer')
    if type(b) == float or type(b) == int:
        b = int(b)
    else:
        raise TypeError('b must be an integer')
    return a + b
