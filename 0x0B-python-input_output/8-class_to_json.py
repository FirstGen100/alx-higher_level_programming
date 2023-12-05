#!/usr/bin/python3
'''
functionreturns dictionary desc wth smp;e data struct for json srialisation'''


def class_to_json(obj):
    '''return a json dictionary'''
    return obj.__dict__
