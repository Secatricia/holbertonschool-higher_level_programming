#!/usr/bin/python3
def max_integer(my_list=[]):
    if(my_list):
        res = 0
        for val in my_list:
            if (val > res):
                res = val
        return (res)
    return (None)
