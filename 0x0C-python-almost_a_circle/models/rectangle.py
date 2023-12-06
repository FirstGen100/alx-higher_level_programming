#!/usr/bin/python3
'''class rectagle inheritig form base'''


from models.base import Base


class Rectangle(Base):
    '''class rectangle'''
    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''width getter'''
        self.__width = width

    @width.setter
    def width(self, value):
        '''width setter'''
        self.__width = value

    @property
    def height(self):
        '''height getter'''
        self.__height = height

    @height.setter
    def height(self, value):
        '''height setter'''
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        self.__x = x

    @x.setter
    def x(self, value):
        '''x setter'''
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        self.__y = y

    @y.setter
    def y(self, value):
        '''y setter'''
        self.__y = value
