#!/usr/bin/python3
"""Write the first class Base"""
import json
import turtle


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

    def draw(list_rectangles, list_squares):
        """define draw function"""
        turtle.setup()
        turtle.bgpic("hippocampes.png")
        turtle.down()
        turtle.color('red', 'yellow')
        for i in list_rectangles:
            turtle.up()
            turtle.forward(i.x)
            turtle.left(90)
            turtle.forward(i.y)
            turtle.left(90)
            turtle.down()
            turtle.fillcolor("darkblue")
            turtle.begin_fill()
            turtle.forward(i.width)
            turtle.left(90)
            turtle.forward(i.height)
            turtle.left(90)
            turtle.forward(i.width)
            turtle.left(90)
            turtle.forward(i.height)
            turtle.left(90)
            turtle.end_fill()

        for j in list_squares:
            turtle.up()
            turtle.forward(i.y)
            turtle.left(90)
            turtle.forward(i.x)
            turtle.left(90)
            turtle.down()
            turtle.fillcolor("lightblue")
            turtle.begin_fill()
            turtle.forward(j.size)
            turtle.left(90)
            turtle.forward(j.size)
            turtle.left(90)
            turtle.forward(j.size)
            turtle.left(90)
            turtle.forward(j.size)
            turtle.left(90)
            turtle.end_fill()

        turtle.up()
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(300)
        turtle.down()
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.circle(50)
        turtle.end_fill()

        turtle.exitonclick()
