#!/usr/bin/python3
""" Defines the square class, inherits from rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class, represents a square"""
    def __init__(self, Size, x=0, y=0, id=None):
        super().__init__(Size, Size, x, y, id)
        self.Size = Size

    @property
    def size(self):
        return self.Size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
        self.Size = value

    def update(self, *args, **kwargs):
        """ Updates the values contained within Square.
        Each value updated depends on the index of args.
        0 = id, 1 = size, 2 = x, 3 = y """
        my_list = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, my_list[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a resumed dictionary reperesentation
        Of the Square class, just variables """
        X = {}
        Y = {}
        for k, v in vars(self).items():
            if 'id' in str(k):
                Y.update({k: v})
            else:
                Y.update({k[12:]: v})
        Y['size'] = Y['']
        Y.pop('')
        Order = ["id", "x", 'size', "y"]
        X = {k: Y[k] for k in Order}
        return X
