#!/usr/bin/python3
"""Create class rectangle"""


class Rectangle:
    """Initialisation width height"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Define width"""
    @property
    def width(self):
        """Recup width"""
        return (self.__width)

    """Define width"""
    @width.setter
    def width(self, value):
        """Test Error"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    """Define height"""
    @property
    def height(self):
        """Recup height"""
        return(self.__height)

    """Define height"""
    @height.setter
    def height(self, value):
        """Test Error"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """Create function that returns the rectangle area"""

    def area(self):
        """return result"""
        return(self.height * self.width)

    """Create function that returns the rectangle perimeter"""

    def perimeter(self):
        """return result"""
        if self.width == 0 or self.height == 0:
            return(0)
        else:
            return(self.width * 2 + self.height * 2)
