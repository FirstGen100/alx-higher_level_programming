#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary.keys())
    for x in sorted_dict:
        print(f'{x}: {a_dictionary[x]}')
