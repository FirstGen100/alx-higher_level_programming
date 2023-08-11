#!/usr/bin/python3
import sys

def print_args(argv):
    length = len(argv) - 1
    count = 1
    if length == 0:
        print('{:d} arguments.'.format(length))
        return
    else:
        if length == 1:
            print('{:d} argument:'.format(length))
        else:
            print('{:d} arguments:'.format(length))
        while count <= length:
            print('{:d}: {:s}'.format(count, argv[count]))
            count += 1

if __name__ == '__main__':
    print_args(sys.argv)
