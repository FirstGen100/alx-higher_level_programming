#!/usr/bin/python3
'''functioin that print text qith 2 lines after . ? : '''


def text_indentation(text):
    '''function that formats text'''
    flag = 1
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        text = text.strip()
        for char in text:
            if flag == 1 and char == ' ':
                continue
            else:
                flag = 0
            print(char, end='')
            if char in ['.', ':', '?']:
                print('\n')
                flag = 1
