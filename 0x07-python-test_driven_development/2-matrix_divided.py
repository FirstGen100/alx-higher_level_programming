#!/usr/bin/python3
'''function that divides all elements of a matrix'''


def matrix_divided(matrix, div):
    '''divides all elements of a matrix'''
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not all(isinstance(row, list) and
               all(isinstance(num, (int, float))
                   for num in row) for row in matrix):
        raise TypeError('matrix must be a matrix' + ' (' +
                        'list of lists' + ') ' + 'of integers/floats')
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    result = [[round(num / div, 2) for num in row] for row in matrix]

    return result
