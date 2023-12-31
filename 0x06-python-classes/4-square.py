#!/usr/bin/python3
"""Square Class
Defines a square based in 3-square.py
"""


class Square:
    """
    defines a square
    """
    def __init__(self, size=0):
        """
        initialise the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """
        get the private sze attribute
        """
        return self.__size

    @size.setter
    def size(self, width):
        """
        Set the value for size
        """
        if not isinstance(width, int):
            raise TypeError("size must be an integer")
        if width < 0:
            raise ValueError("size must be >= 0")
        self.__size = width

    def area(self):
        """
        find area of the square
        """
        return (self.__size * self.__size)
