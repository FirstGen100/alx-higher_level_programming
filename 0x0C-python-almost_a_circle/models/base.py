#!/usr/bin/python3
'''
The base class
'''
import json


class Base:
    '''class base'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as file:
            jsonstring = cls.to_json_string([obj.to_dictionary()
                                            for obj in list_objs])
            file.write(jsonstring)

    @staticmethod
    def from_json_string(json_string):
        '''
        return list of the json representation
        '''

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all the attributes set
        '''

        if cls.__name__ == 'Rectangle':
            dummyinstance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummyinstance = cls(1)
        else:
            dummyinstance = cls()
        dummyinstance.update(**dictionary)
        return dummyinstance
