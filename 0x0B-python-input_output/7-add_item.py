#!/usr/bin/python3
'''
function to ass arguments to a list and save them to a file
'''

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def get_arguments(arguments):
    '''
    write arguments to a list
    '''

    try:
        my_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        my_list = []
    my_list.extend(arguments)
    save_to_json_file(my_list, 'add_item.json')


if __name__ == '__main__':
    arguments = sys.argv[1:]
    get_arguments(arguments)
