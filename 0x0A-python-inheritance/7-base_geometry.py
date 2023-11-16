#!/usr/bin/python3
'''class based on prev 6-base-geometry'''


class BaseGeometry:
    '''implement an empty area func amd integer validator'''
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validates a value'''
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
