#!/usr/bin/python3
'''function that writes string to text file and return chars'''


def write_file(filename='', text=''):
    '''write and count a string'''
    with open(filename, 'w', encoding='utf8') as file:
        file.write(text)
        return len(text)
