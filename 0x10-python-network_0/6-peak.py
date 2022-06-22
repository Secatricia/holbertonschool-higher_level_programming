#!/usr/bin/python3
#Write a function that finds a peak in a list of unsorted integers

def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers
    """
    size = len(list_of_integers)
    size_cp = size
    size_two = size // 2

    if size == 0:
        return None

    while True:
        size_cp = size_cp // 2
        if (size_two < size - 1 and
                list_of_integers[size_two] < list_of_integers[size_two + 1]):
            if size_cp // 2 == 0:
                size_cp = 2
            size_two = size_two + size_cp // 2
        elif size_cp > 0 and list_of_integers[size_two] < list_of_integers[size_two - 1]:
            if size_cp // 2 == 0:
                size_cp = 2
            size_two = size_two - size_cp // 2
        else:
            return list_of_integers[size_two]