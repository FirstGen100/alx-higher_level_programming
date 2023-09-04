#!/usr/bin/python3
"""Square Class
Define a square based on 1-square.py
"""


class Square:
    """
    Define a square blueprint
    """
    def __init__(self, size=0):
        """Init constructor
        Initialise square with size variable
        Arg:
            size: integer
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        else:
            self.__size = size
