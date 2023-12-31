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
        try:
            Args = ('id', 'size', 'x', 'y')
            for i, arg in enumerate(args):
                setattr(self, Args[i], arg)
        except TypeError:
            pass
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        '''return dictionary represent of square'''
        args = ['id', 'size', 'x', 'y']
        new = {}
        for i in args:
            value = getattr(self, i)
            new.update({i: value})
        return new
