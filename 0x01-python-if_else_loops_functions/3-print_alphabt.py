#!/usr/bin/python3
for i in range(65, 91):
    if i == 69 or i == 81:
        continue
    else:
        print("{:c}".format(i), end='')
