#!/usr/bin/python3

from add_0 import add

add.a = 1
add.b = 2

Sum = add.a + add.b

print("{:d} + {:d} = {:d}".format(add.a, add.b, Sum))
