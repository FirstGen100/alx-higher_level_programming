#!/usr/bin/python3
'''rectangle class based on prev 8-rectangle'''


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
    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
         return self.__width * self.__height

    def __str__(self):
        return (f'[Rectangle] {self.__width}/{self.__height}')
