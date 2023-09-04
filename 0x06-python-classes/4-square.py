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
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        find area of the square
        """
        return (self.__size * self.__size)
