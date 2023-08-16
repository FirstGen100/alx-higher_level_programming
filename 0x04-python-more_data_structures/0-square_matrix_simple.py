#!/usr/bin/python3
def square_matrix(matrix=[]):
    temp = []
    for x in matrix:
        temp.append(list(map(lambda x: x**2, x)))
    return temp
