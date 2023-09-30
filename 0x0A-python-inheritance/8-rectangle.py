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
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


'''rectangle class'''
class Rectangle(BaseGeometry):


    '''class inherits from BaseGeometry'''
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__height = height
        self.__width = width