#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
i = number
if number < 0:
    i = ((-number) % 10) * 1
while i > 9:
    i = number % 10
print("Last digit of {:d} is {:d} " .format(number, i), end="")

if i > 5:
    print("and is greater than 5")
elif i == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
