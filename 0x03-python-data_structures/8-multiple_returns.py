#!/usr/bin/python3
def multiple_returns(sentence):
    len_string = len(sentence)
    char_1 = sentence[0]
    x_string = (len_string, char_1)
    if len_string == 0:
        char_1 = "None"
        return x_string
    else:
        len_string = len(sentence)
        char_1 = sentence[0]
        return x_string
