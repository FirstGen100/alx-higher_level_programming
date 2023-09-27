#!/usr/bin/python3
'''class that inherits from list'''


class MyList(list):
    '''class that inherits from list'''

    def print_sorted(self):
        '''prints the sorted list(ascending)'''
        print(sorted(self))
