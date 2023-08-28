#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    
    for i in range(list_lenght):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            res = 0
        except IndexError:
            print("Out of range")
            res = 0
        finally:
            new_list.append(res)
    return new_list
