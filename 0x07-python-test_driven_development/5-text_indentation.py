#!/usr/bin/python3
'''
prints a text with 2 new lines after the characters . , ? and :
'''


def text_indentation(text):
    '''
    adds 2 new lines after the characters ., ? and :
    '''
    flag = 1
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        text = text.strip()
        for x in text:
            if flag == 1 and x == ' ':
                continue
            else:
                flag = 0
            print(x, end='')
            if x in ['.', '?', ':']:
                print('\n')
                flag = 1
