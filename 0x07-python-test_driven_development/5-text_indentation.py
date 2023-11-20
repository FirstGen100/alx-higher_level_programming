#!/usr/bin/python3
'''functioin that print text qith 2 lines after . ? : '''


def text_indentation(text):
    '''function that formats text'''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    result = []
    text = list(text)
    for char in range(0, len(text)):
        result.append(text[char])
        if text[char] == '.':
            result.append('\n\n')
        if text[char] == '?':
            result.append('\n\n')
        if text[char] == ':':
            result.append('\n\n')
    print(''.join(result), end='')
