#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("{} must be an integer".format(self))
        if width <= 0:
            raise ValueError("{} must be > 0".format(self))
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("{} must be an integer".format(self))
        if height <= 0:
            raise ValueError("{} must be > 0".format(self))
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("{} must be an integer".format(self))
        if x < 0:
            raise ValueError("{} must be >= 0".format(self))
        self.__x = x

    @property
    def y(self):
        return self.__y

    @x.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("{} must be an integer".format(self))
        if y < 0:
            raise ValueError("{} must be >= 0".format(self))
        self.__y = y
