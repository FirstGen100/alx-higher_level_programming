#!/usr/bin/python3
'''class that inherits from list'''


class MyList(list):
    '''initialisation of the class'''
    def __init__(self):
        pass
    
    def print_sorted(self):
        '''prints the sorted list(ascending)'''
        print(sorted(self))
