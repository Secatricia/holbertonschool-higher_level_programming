#!/usr/bin/python3
def max_integer(my_list=[]):
    res = 0
    if(len(my_list) == 0):
        return (None)
    for val in my_list:
        if (val > res):
            res = val
    return (res)
