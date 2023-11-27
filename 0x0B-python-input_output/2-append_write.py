#!/usr/bin/python3
'''funtion that appends string to end of text file'''


def append_write(filename='', text=''):
    '''appends string to end of file'''
    with open(filename, 'a', encoding='utf8') as file:
        file.write(text)
        return len(text)
