#!/usr/bin/python3
"""function that appends a string at the end
of a text file (UTF8) and returns the number
of characters added"""


def append_write(filename="", text=""):
    """Create function append_write"""
    with open(filename, "a", encoding='UTF8') as fp:
        nb = fp.write(text)
        return nb
