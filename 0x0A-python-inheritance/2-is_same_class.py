#!/usr/bin/python3
""" returns True if the object is exactly an instance
of the specified class ; otherwise False."""


def is_same_class(obj, a_class):
    """Return True or False"""
    if type(obj) == a_class:
        return True
    else:
        return False
