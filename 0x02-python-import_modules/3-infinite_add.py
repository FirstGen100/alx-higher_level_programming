#!/usr/bin/python3
import sys

def add_args(argv):
    length = len(argv) - 1
    count = 1
    add = 0

    if length == 0:
        print('{:d}'.format(length))
        return
    else:
        while count <= length:
            add += int(argv[count])
            count += 1
        print('{:d}'.format(add))

if __name__ == '__main__':
    add_args(sys.argv)
