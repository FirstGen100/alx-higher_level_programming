#!/usr/bin/python3
''' function that prints a square with char #'''


def print_square(size):
    '''prints a square using #'''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if isinstance(size, float) and size < 0:
        raise Exception('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for _ in range(size):
        print('#' * size)
