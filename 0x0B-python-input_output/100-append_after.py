#!/usr/bin/python3
'''fuction to insert text after line containing a specified text'''


def append_after(filename='', search_string='', new_string=''):
    '''insert text to file after string'''
    with open(filename, 'r') as file:
        line = file.readlines()

    with open(filename, 'w') as file:
        for l in line:
            file.write(l)
            if search_string in l:
                file.write(new_string + '\n')
