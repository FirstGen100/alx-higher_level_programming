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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return (json.dumps(list_dictionaries))
    
    @staticmethod
    def save_to_file(cls, list_objs):
        '''writes json string to file'''
        if list_objs:
            lists = [obj.to_dictionary() for obj in list_objs]
        else:
            lists = []
        with open(cls.__name__ + '.json', 'w') as file:
            file.write(cls.to_json_string(lists))
