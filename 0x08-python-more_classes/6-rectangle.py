#!/usr/bin/python3
'''
Defines a rectnagle
'''


class Rectangle:
    '''
    Define a rectangle and set the properties
    '''
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        ''' returns the area of the rectagle '''

        return self.__height * self.__width

    def perimeter(self):
        ''' returns the erimeter of the rectangle '''

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        string = ''
        if self.__width != 0 and self.__height != 0:
            string += '\n'.join('#' * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        '''return repr of an obj that can be used by eval to create new obj'''
        string = 'Rectangle' + '(' + str(self.__width) + ', '
        string += str(self.__height) + ')'
        return string

    def __del__(self):
        number_of_instances -= 1
        print('Bye rectangle...')
