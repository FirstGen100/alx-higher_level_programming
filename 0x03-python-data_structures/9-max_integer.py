#!/usr/bin/python3
def max_integer(my_list=[]):
    len_list = len(my_list)
    max_num = my_list[0]

    if len_list == 0:
        return None
    for i in my_list:
        if i > max_num:
            max_num = i
    return max_num
