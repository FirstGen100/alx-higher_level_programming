#!/usr/bin/python3
def multiple_returns(sentence):
    len_string = len(sentence)
    x_string = ()
    if len_string > 0:
        char_1 = sentence[0]
        x_string = len_string, char_1
    else:
        x_string = len_string, 'None'
    return x_string
