#!/usr/bin/python3

''' locked class that only allow instance attribute called first_name '''


class LockedClass:

    ''' locked class '''
    __slots__ = ['first_name']
