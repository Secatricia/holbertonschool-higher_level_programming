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

    @staticmethod
    def to_json_string(list_dictionaries):
        """define to_json_string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """define save_to_file function"""
        file = cls.__name__ + ".json"
        dict_objet = []
        if list_objs is None:
            list_objs = {}

        for val in list_objs:
            dict_objet.append(val.to_dictionary())

        list_str = cls.to_json_string(dict_objet)

        with open(file, 'w+') as fp:
            fp.write(list_str)
        fp.close

    def from_json_string(json_string):
        """define from_json_string function"""
        if json_string is None:
            json_string = {}
            return json_string
        else:
            return json.loads(json_string)
