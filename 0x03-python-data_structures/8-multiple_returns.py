#!/usr/bin/python3
def multiple_returns(sentence):
    len_string = len(sentence)
    char_1 = sentence[0]
    if sentence is None:
        return
    else:
        x_string = (len_string, char_1)
        return x_string
