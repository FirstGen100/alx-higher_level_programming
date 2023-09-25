#!/usr/bin/python3

'''
module to add integers
'''
def add_integer(a, b=98):
    '''
    function to add integers
    '''
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) or isinstance(b, bool):
        raise TypeError('b must be an integer')
    return (a + b)
