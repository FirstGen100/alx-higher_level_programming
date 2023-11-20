#!/usr/bin/python3
'''function to multiply matrices'''


def matrix_mul(m_a, m_b):
    '''multiply 2 matrices'''
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    elif not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError('m_b should contain only integers or floats')

    row_s_a = len(m_a[0])
    row_s_b = len(m_b[0])
    if not all(len(row) == row_s_a for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(row) == row_s_b for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    col_s_a = len(m_a[0])
    row_s_b = len(m_b)
    if col_s_a != row_s_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]
    return result
