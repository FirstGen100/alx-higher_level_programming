#!/usr/bin/python3
'''class square'''

Rectangle = __import__('9-rectangle').Rectangle


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
