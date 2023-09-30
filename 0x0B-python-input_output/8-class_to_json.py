#!/usr/bin/python3
'''
function that returns dictionary desc of json serialisation of an object
'''


def class_to_json(obj):
    '''
    returns the dictionary description for json serialisation of an object
    '''

    if isinstance(obj, bool) or isinstance(obj, int) or isinstance(obj, str):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        return {class_to_json(key): class_to_json(value) for key, value in obj.items()}
    else:
        return {class_to_json(key): class_to_json(value) for key, value in obj.__dict__.items()}
