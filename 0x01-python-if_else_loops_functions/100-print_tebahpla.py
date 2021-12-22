#!/usr/bin/python3
i = 122
while i != 96:
    if (i % 2) == 0:
        print(chr(i), end="")
        i -= 1
    else:
        print(chr(i - 32), end="")
        i -= 1
