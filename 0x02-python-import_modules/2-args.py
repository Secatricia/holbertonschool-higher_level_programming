#!/usr/bin/python3
from sys import argv
i = 0
j = len(argv) - 1
if __name__ == '__main__':
    if j == 0:
        print("{} arguments.".format(j))
    elif j == 1:
        print("{} argument:".format(j))
    else:
        print("{} arguments:".format(j))
    while (i < j):
        i += 1
        print("{}: {}".format(i, argv[i]))
