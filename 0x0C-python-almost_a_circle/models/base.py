#!/usr/bin/python3
'''first class base'''

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''convert to json string'''
        if list_dictionaries is None:
            return '[]'
        elif any(type(i) != dict for i in list_dictionaries):
            pass
        else:
            return json.dumps(list_dictionaries)
    
    @staticmethod
    def save_to_file(cls, list_objs):
        '''writes json string to file'''
        if list_objs is None or list_objs == []:
            new = []
        else:
            f = type(list_objs[0])
            if any(type(i) != f for i in list_objs):
                pass
            new = [i.to_dictionary() for i in list_objs]
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(new))
