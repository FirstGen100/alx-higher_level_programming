#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


'''square class'''


class Square(Rectangle):
    '''class square'''

    def __init__(self, size):
        Rectangle.__init__(self, size, size)
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f'[Square] {self.__size}/{self.__size}'

    def __repr__(self):
        return str(self)
