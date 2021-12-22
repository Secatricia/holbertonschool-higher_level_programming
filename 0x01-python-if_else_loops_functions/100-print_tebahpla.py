#!/usr/bin/python3
for i in range(97, 123)[::-1]:
    if (i % 2) != 0:
        i -= 32
    print(chr(i), end="")
    if i > 64 and i < 91:
        i += 32
