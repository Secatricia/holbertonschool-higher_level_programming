#!/bin/usr/python3
from unittest import result


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    list_res = []
    result = 0
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            list_res.append(result)
    return (list_res)