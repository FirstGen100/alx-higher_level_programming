#!usr/bin/python3
'''
functionreturns dictionary desc wth smp;e data struct for json srialisation'''


import json


def class_to_json(obj):
    '''return a json dictionary'''
    my_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, list) or isinstance(value, dict):
            my_dict[key] = class_to_json(value)
        elif isinstance(value, (str, int, bool)):
            my_dict[key] = value

    return my_dict
