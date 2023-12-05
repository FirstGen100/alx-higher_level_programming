#!/usr/bin/python3
'''first class base'''


class Base:
    ''' the base tracking class'''
    __nb_objects = 0
    
    def __init__(self, id=None):
        '''init constructor'''
        if id is not None:
            self.id = id
        else:
            self.__class__. __nb_objects += 1
            self.id = self.__class__.__nb_objects
