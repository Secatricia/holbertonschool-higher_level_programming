#!/usr/bin/python3
"""class Student that defines a student by"""


class Student:
    """init class"""

    def __init__(self, first_name, last_name, age):
        """define init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """define to_json function"""
        return vars(self)
