#!/usr/bin/python3
'''the square class inheriting rectangle class'''


from models.rectangle import Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self. width = value
        self.height = value

    def __str__(self):
        '''overwride str'''
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.size)

    def update(self, *args, **kwargs):
        '''assigns attributes'''
        for key, value in kwargs.items():
            setattr(self, key, value)
