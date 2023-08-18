#!/usr/bin/python3
def multiple_returns(sentence):
    len_string = len(sentence)
    if len_string == 0:
        char_1 = "None"
        x_string = (len_string, char_1)
        return x_string
    else:
        char_1 = sentence[0]
        return x_string
