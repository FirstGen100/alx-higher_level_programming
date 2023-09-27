#!/usr/bin/python3
'''empty class'''


class BaseGeometry:
    '''empty area class'''

    def area(self):
        '''returns area'''
        return width * height

    def integer_validator(self, name, value):
        '''validates the value'''

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')

'''rectangle class'''
class Rectangle(BaseGeometry):
    '''class inherits from BaseGeometry'''

    def __init__(self, width, height):
        if BaseGeometry.integer_validator(self, 'width', width):
            self.__width = width
        if BaseGeometry.integer_validator(self, 'height', height):
            self.__height = height

    def __str__(self):
        print(f'[Rectangle] {self.__height} {self.__width}')
