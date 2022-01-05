#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    new.update((i, j * 2) for i, j in new.items())
    return new
