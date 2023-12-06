#!/usr/bin/python3
'''class rectagle inheritig form base'''


from models.base import Base


class Rectangle(Base):
    '''class rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height setter'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        '''x setter'''
        if type(value) != int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        '''y setter'''
        if type(value) != int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        '''return area of rectangle'''
        return self.__width * self.__height

    def display(self):
        '''display the rectangle as #'''
        print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        '''overwride the str method'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                                                       self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        '''
        assigns an agument to each attribute
        Args = ('id', 'width', 'height', 'x', 'y')
        for i, arg in enumerate(args):
            setattr(self, Args[i], arg)
        '''
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        '''returns dict representation of a rectangle'''
        return self.__dict__
