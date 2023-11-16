#!/usr/bin/python3
'''prints a sorted list'''


class MyList(list):
    '''sorts a list in ascending order'''
    def print_sorted(self):
        print(sorted(self))
