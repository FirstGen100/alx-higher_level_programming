#!/usr/bin/python3
'''function that reads a text fie and prints to stdout'''


def read_file(filename=''):
    '''read file abd prnt to stdout'''
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            print(line, end='')
