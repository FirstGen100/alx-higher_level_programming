#!/usr/bin/python3

class myclass:
    def __init__(self, name):
        self.name = name
        self.number = 0
    def __str__(self):
        return "[myclass] {} - {:d}".format(self.name, self.number)
