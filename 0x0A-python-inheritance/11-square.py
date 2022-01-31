#!/usr/bin/python3
"""class Square that inherits from Rectangle
(9-rectangle.py). (task based on 10-square.py)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square:
    """Create class that define Square"""

    def __init__(self, size):
        """Create Rectangle class"""
        self.__size = size

    def area(self):
        """Function that return square area"""
        return (self.__size * self.__size)

    def __str__(self):
        """print info"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
