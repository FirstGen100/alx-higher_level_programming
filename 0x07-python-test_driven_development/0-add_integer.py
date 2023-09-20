#!/usr/bin/python3


def add_integer(a, b=98):
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError('a must be an integer')
    elif not isinstance(b, int) or isinstance(b, bool):
        raise TypeError('b must be an integer')
    return (a + b)
