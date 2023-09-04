#!/usr/bin/python3
"""Square Class
Defines a square based in 4-square.py
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

    def my_print(self):
        """
        prints in stdout the square wuth the char # or an wmpty line
        """
        if self.__size <= 0:
            print('')
        else:
            for x in range(self.size):
                for y in range(self.size):
                    print('#', end='\n'if y is self.size - 1 and x != y else'')
            print()
