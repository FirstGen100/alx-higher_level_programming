#!/usr/bin/python3
'''function that erites an object to a text file'''


import json


def save_to_json_file(my_obj, filename):
    '''writes an object to text file'''
    with open(filename, 'w', encoding='utf8') as file:
        json.dump(my_obj, file)
