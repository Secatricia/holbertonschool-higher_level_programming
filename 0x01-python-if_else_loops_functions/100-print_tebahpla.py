#!/usr/bin/python3
i = 122
while i != 96:
    if (i % 2) != 0:
        i -= 32
    print(chr(i), end="")
    if i > 64 and i < 91:
        i += 32
    i -= 1
