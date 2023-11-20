#!/usr/bin/python3
'''functioin that print text qith 2 lines after . ? : '''


def text_indentation(text):
    '''function that formats text'''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    result = ''
    for char in text:
        if char in ['.', '?', ':']:
            result += '\n\n'
        else:
            result += char
    result = result.strip()
    print(result)
