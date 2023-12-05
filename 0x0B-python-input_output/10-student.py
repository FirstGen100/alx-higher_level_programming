#!/usr/bin/python3
''' class student '''


class Student:
    '''defines a student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        '''retrieve instance rep of Student'''
        if attr is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attr if
                    hasattr(self, attr)}
