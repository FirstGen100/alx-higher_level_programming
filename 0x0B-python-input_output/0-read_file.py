#!/usr/bin/python3
'''function that reads a text fie and prints to stdout'''


def read_file(filename=''):
    '''read file abd prnt to stdout'''
    file = open(filename)
    file =file.read(w, file)
    print(file)
    file.close()
