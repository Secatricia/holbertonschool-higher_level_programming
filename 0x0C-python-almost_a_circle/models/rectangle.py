#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Define Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise __init__ function"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """define width function"""
        return self.__width

    @width.setter
    def width(self, width):
        """define width function"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """define height function"""
        return self.__height

    @height.setter
    def height(self, height):
        """define height function"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """define x function"""
        return self.__x

    @x.setter
    def x(self, x):
        """define x function"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """define y function"""
        return self.__y

    @x.setter
    def y(self, y):
        """define y function"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Define area function"""
        return self.height * self.width

    def display(self):
        """define display function"""
        for i in range(self.__y):
            print()
        for j in range(self.height):
            for m in range(self.__x):
                print(" ", end="")
            for k in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """define __str__ function"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.width, self.height))
