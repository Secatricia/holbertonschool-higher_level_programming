#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("The string Last digit of {:d} " .format(number), end="")
if number < 0:
    number = number * (-1)
while number > 9:
    number = number % 10
if number > 5:
    print("and is greater than 5")
elif number == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
