#!/usr/bin/python3
'''rectangle class inheriting base-geometry'''


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


class Rectangle(BaseGeometry):
    '''instanciating the variables'''
    def __init__(self, width, height):
        bg = BaseGeometry()
        bg.integer_validator('height', height)
        bg.integer_validator('width', width)
        self.__height = height
        self.__width = width
