#!/usr/bin/python3
'''empty class'''


class BaseGeometry:
    '''empty area class'''

    def area(self):
        '''returns area'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''validates the value'''

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


''' class rectangle'''


class Rectangle(BaseGeometry):
    '''class rectangle'''

    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__height = height
        self.__width = width
