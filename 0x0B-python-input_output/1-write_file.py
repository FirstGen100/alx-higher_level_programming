#!/usr/bin/python3
'''
write to a txt file
'''


def write_file(filename='', text=''):
    '''
    write content of filename to text
    '''

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
