#!/usr/bin/python3
'''
function pascal triangle:
    returns list of lists of integers representing the triangle n
'''


def pascal_triangle(n):
    '''
    function returns lis of integers rep a pascal triangle
    '''

    my_list = [[1]]
    if n <= 0:
        my_list = []
        return my_list
    else:
        for x in range(1, n):
            row = [1]
            for y in range(1, x):
                value = my_list[x-1][y-1] + my_list[x-1][y]
                row.append(value)
            row.append(1)
            my_list.append(row)
        return my_list
