#!/usr/bin/python3
import calculator_1 as f
a = 10
b = 5
print("{:d} + {:d} = {} ".format(a, b, f.add(a, b)))
print("{:d} - {:d} = {}".format(a, b, f.sub(a, b)))
print("{:d} * {:d} = {}".format(a, b, f.mul(a, b)))
print("{:d} / {:d} = {}".format(a, b, f.div(a, b)))
