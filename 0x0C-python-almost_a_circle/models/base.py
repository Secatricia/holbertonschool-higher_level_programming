#!/usr/bin/python3
"""Write the first class Base"""
import json


class Base:
    """define class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """intitialise id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """define to_json_string"""
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        if list_objs is None:
            pass
