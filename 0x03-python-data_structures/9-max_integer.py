#!/usr/bin/python3
from typing import Sequence


def max_integer(my_list=[]):
    res = 0
    if( len(my_list) == 0):
        return None
    for i in range(len(my_list)):
        if (my_list[i] > res):
            res = my_list[i]
    return res
