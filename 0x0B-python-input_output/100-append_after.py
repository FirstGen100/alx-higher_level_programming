#!/usr/bin/python3
'''fuction to insert text after line containing a specified text'''


def append_after(filename='', search_string='', new_string=''):
    '''insert text to file after string'''
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
