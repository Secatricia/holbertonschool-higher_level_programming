#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Create Rectangle class"""
    def __init__(self, width, height):
        """Create __init__ function"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
