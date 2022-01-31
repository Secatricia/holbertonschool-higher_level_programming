#!/usr/bin/python3
"""class BaseGeometry (based on 5-base_geometry.py)"""


class BaseGeometry:
    """Create BaseGeometry class"""

    def area(self):
        """Raise Error"""
        raise Exception("area() is not implemented")

    """Create function that raise Error"""

    def integer_validator(self, name, value):
        """Test with value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be greater than 0".format(name))


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
