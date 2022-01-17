#!/bin/usr/python3
from ast import Return
from pickle import FALSE, TRUE


def safe_print_integer(value):
    try:
        if type(value) == int:
            print("{}".format(value))
            return(True)
    except ValueError:
        Return(False)
