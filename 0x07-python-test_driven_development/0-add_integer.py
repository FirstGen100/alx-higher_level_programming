#!/usr/bin/python3


'''
module to add integers
'''
def add_integer(a, b):
    '''
    function to add integers
    '''
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int):
        raise TypeError('b must be an integer')
    else:
        return (a + b)
