#!/usr/bin/python3
'''funtion that creates object from json file'''


import json


def load_from_json_file(filename):
    '''create object frim a jon file'''
    with open(filename, 'r') as file:
        return json.loads(file.read())
