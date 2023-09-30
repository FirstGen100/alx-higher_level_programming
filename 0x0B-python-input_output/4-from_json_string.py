#!/usr/bin/python3
'''
Returns an object represented by a json string
'''

import json


def from_json_string(my_str):
    '''
    return a json str to py object
    '''

    return json.loads(my_str)
