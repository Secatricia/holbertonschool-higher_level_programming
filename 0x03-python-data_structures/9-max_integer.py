#!/usr/bin/python3
def max_integer(my_list=[]):
    res = 0
    if(my_list):
        return (None)
    for val in my_list:
        if (val > res):
            res = val
    return (res)
