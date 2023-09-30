#!/usr/bin/python3
'''
function to append a file
'''

def append_write(filename='', text=''):
    '''append to a file'''

    with open(filename, 'a', encoding='utf-8') as file:
        text.write(text)
        return len(text)
