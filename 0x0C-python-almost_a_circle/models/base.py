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
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return '[]'
