#!/usr/bin/python3
'''
divides all the elements of a matrix
'''


def matrix_divided(matrix, div):
    '''
    divides all the elements of a matrix
    '''
    size = None
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for l in matrix:
        if type(l) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if size is None:
            size = len(l)
        elif size != len(l):
            raise TypeError("Each row of the matrix must have the same size")
        for i in l:
            if type(i) is not int and type(i) is not float:
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            if type(div) is not int and type(div) is not float:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            return [[round(i / div, 2) for i in l] for l in matrix]
