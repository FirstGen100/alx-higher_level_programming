#!/usr/bin/python3
'''
divides all the elements of a matrix
'''


def matrix_divided(matrix, div):
    '''
    divides all the elements of a matrix
    '''
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix 
                                               or not all(isinstance(num, (int, float))\
    for row in matrix for num in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    rows = set(len(row) for row in matrix)
    if len(rows) > 1:
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    newm = [[round(num / div, 2) for num in row] for row in matrix]
    return newm
