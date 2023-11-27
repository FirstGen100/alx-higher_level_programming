#!/usr/bin/python3
'''adds all arguments to a list and save to file'''


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys

if __name__ == '__main__':
    filename = 'add_item.json'
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list =[]

    new = my_list + sys.argv[1:]
    save_to_json_file(new, filename)

