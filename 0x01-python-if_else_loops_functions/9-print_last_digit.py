#!/usr/bin/python3
def print_last_digit(number):
    ptr = 0
    if number < 0:
        number *= -1
        ptr = 1
    last_digit = number % 10
    if ptr == 1:
        number *= -1
    print('{:d}'.format(last_digit), end="")
    return last_digit
