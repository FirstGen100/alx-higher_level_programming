#!/usr/bin/python3
''' returns true if object is an instance if a class '''


def inherits_from(obj, a_class):
    '''checks if ibj is an instance if a class'''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
