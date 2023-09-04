#!/usr/bin/python3
"""Square Class
Defines a square based in 4-square.py
"""


class Square:
    """
    defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialise the size of the square
        """
        self.__size = size
        if (not isinstance(position, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not isinstance(position[0], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif(not isinstance(position[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """
        get position private variable
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        tuple of 2 positive integers
        """
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        find area of the square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        prints in stdout the square wuth the char # or an wmpty line
        """
        if self.__size == 0:
            print('')
        else:
            for x in range(self.position[1]):
                print()
            for x in range(self.size):
                for y in range(self.position[0]):
                    print(' ', end='')
                for y in range(self.size):
                    print('#', end='')
                print()
