#!/usr/bin/python3
'''
functionto return json rep of an object
'''


import json


def to_json_string(myobj):
    '''
    json rep of a string
    '''

    return json.dumps(myobj)
