#!/usr/bin/python3
""" class Student that defines a student by:
(based on 9-student.py)"""


class Student:
    """init class"""

    def __init__(self, first_name, last_name, age):
        """define init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation
        of a Student instance (same as 8-class_to_json.py)"""
        if type(attrs) is list:
            return {i: self.__dict__.get(i) for i in attrs
                    if i in self.__dict__}
        return vars(self)

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for x, y in json.items():
            setattr(self, x, y)
