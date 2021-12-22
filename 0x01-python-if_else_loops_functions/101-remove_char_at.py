#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    lettre = ""
    while i < len(str):
        if i != n:
            lettre = lettre + str[i]
        i += 1
    return lettre
