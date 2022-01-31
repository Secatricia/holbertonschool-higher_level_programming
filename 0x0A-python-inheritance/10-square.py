#!/usr/bin/python3
"""class Square that inherits from Rectangle
(9-rectangle.py)"""
Rectangle = __import__('9-rectangle').Rectangle

class Square:
    def __init__(self, size):
        """Create Rectangle class"""
        self.__size = size

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
