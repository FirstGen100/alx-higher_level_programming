#!/usr/bin/python3
'''
writes an object file to a text file using json rep
'''

import json


def save_to_json_file(my_obj, filename):
    '''
    write json rep to a file
    '''

    with open(filename, 'w') as file:
        jsonfile = json.dumps(my_obj)
        file.write(jsonfile)
        return jsonfile
