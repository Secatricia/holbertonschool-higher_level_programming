#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """define square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """define size function"""
        return self.width

    @size.setter
    def size(self, size):
        """define width function"""
        self.width = size
        self.height = size

    def __str__(self):
        """define __str__ function"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """define update function"""
        tab = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, tab[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in tab:
                    setattr(self, key, value)

    def to_dictionary(self):
        """define to_dictionary function"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
