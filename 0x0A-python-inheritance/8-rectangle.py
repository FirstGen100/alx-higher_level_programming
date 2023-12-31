#!/usr/bin/python3
'''rectangle class inheriting base-geometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''instanciating the variables'''
    def __init__(self, width, height):
        super().integer_validator('height', height)
        super().integer_validator('width', width)
        self.__height = height
        self.__width = width
