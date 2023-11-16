#!/usr/bin/python3
''' checks if object and class types match '''


def is_same_class(obj, a_class):
    ''' returns true if an object is exactly an instamce of the class '''
    return type(obj) is a_class
