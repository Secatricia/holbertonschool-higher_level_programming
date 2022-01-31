#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""class Rectangle that inherits from
BaseGeometry (7-base_geometry.py)"""


class Rectangle(BaseGeometry):
    """Initialise width and height"""

    def __init__(self, width, height):
        """Call integer_validator"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
