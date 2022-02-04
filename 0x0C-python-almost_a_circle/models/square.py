#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """define square class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

        def __str__(self):
            """define __str__ function"""
            return ("[Square] ({}) {}/{} - {}/{}".format(self.id,
                    self.__x, self.__y, self.size, self.size))
