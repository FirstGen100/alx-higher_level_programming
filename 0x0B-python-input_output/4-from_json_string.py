#!/usr/bin/python3
'''retruns an object represented by a json string'''


import json


def from_json_string(my_str):
    '''returns a json load string'''
    return json.loads(my_str)
