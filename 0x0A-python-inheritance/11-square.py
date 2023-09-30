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


'''rectangle class'''


class Rectangle(BaseGeometry):
    '''class rectangle'''

    def __init__(self, width, height):
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f'[Rectangle] {self.__width}/{self.__height}'

    def __repr__(self):
        return str(self)


'''square class'''


class Square(Rectangle):
    '''class square'''

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator('width', size)
        self.__size = size

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'

    def __repr__(self):
        return str(self)
