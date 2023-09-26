#!/usr/bin/python3
'''
prints a text with 2 new lines after the characters . , ? and :
'''


def text_indentation(text):
    '''
    adds 2 new lines after the characters ., ? and :
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for x in text:
        if x == '.' or x == '?' or x == ':':
            print(x)
            print()
            print()
        else:
            print(x, end='')
