#!/usr/bin/python3
"""class Square"""


class Square:
    """ define __size"""

    def __init__(self, size=0, position=(0, 0)):

        self.__size = size
        self.value = position

    """Return size"""

    @property
    def size(self):

        return(self.__size)

    """define value"""

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
        return (value)

    """Return square area"""

    def area(self):

        return(self.__size * self.__size)

    """initialisation position"""

    @property
    def position(self):
        return (self.position)

    """definition position"""
    @position.setter
    def position(self, value):

        if self.position[1] < 0 or self.position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    """Print squares"""

    def my_print(self):

        if self.__size == 0:
            print()
            return()

        for i in range(self.__size):
            for k in range(self.position[0]):
                print()
            for j in range(self.__size):
                print("#", end="")
            print()
