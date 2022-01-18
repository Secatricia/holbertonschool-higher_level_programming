#!/usr/bin/python3
"""class Square"""


class Square:
    """ define __size"""

    def __init__(self, size=0):

        self.__size = size

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
