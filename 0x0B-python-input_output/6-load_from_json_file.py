#!/usr/bin/python3
'''
function that creates an object from a Json file
'''

import json


def load_from_json_file(filename):
    '''
    create onject from jso file
    '''

    with open(filename, 'r') as file:
        jsonfile = file.read()
        return json.loads(jsonfile)
