#!/usr/bin/python3

x = 122
while x >= 97:
    flag = 0
    if x % 2 != 0:
        x = x - 32
        flag = 1
    print('{:s}'.format(chr(x)), end="")
    if flag == 1:
        x = x + 32
    x = x - 1
