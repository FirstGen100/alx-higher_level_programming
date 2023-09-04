#!/usr/bin/python3
"""
Rectangle Class
empty class to define a rectangle
"""

class Rectangle:
    """ Define an empty rectangle"""
    def __init__(self, width=0, height=0):
        '''
        initialise class variables
        '''
        self.__width = width
        self.__height = height
    
    @property
    def height(self):
        '''
        get height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
        set height
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
    @property
    def width(self):
        '''
        get width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        set width
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
    def area(self):
        '''
        find the area of the rectangle
        '''
        return self.height * self.width
    def perimeter(self):
        '''
        find the rectagle perimeter
        '''
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height + self.width) * 2
