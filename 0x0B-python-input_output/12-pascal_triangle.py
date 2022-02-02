#!/usr/bin/python3
""" function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """define pascal triangle function"""
    list = []
    if n <= 0:
        return list
    
    tp = [[1]]

    while len(tp) != n:
        triangle = tp[-1]
        tmp = [1]
        size = len(triangle)
        for i in range(size - 1):
            tmp.append(triangle[i] + triangle[i + 1])
        tmp.append(1)
        tp.append(tmp)

    return (tp)