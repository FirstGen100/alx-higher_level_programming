#!/usr/bin/python3
"""
Rectangle Class
empty class to define a rectangle
"""


class Rectangle:
    """ Define an empty rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''initialise class variables'''
        Rectangle.number_of_instances += 1
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError('Height must be an integer')
        elif height < 0:
            raise ValueError('Height must be >= 0')
        else:
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
        return self.__height * self.__width

    def perimeter(self):
        '''
        find the rectagle perimeter
        '''
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        '''
        Returns the string
        '''
        if self.__width == 0 or self.__height == 0:
            return ''
        rep_str = ''
        rep_str = '\n'.join([str(self.print_symbol) * self.__width
                            for _ in range(self.__height)])
        return rep_str

    def __repr__(self):
        return (f'Rectangle({self.__width}, {self.__height})')

    def __del__(self):
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
