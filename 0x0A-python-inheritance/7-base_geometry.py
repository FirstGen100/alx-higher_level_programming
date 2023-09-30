#!/usr/bin/python3
'''empty class'''


class BaseGeometry:
    '''empty area class'''

    def area(self):
        '''returns area'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validates the value'''

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')