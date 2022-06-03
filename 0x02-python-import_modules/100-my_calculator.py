#!/usr/bin/python3

from calculator_1 import add, sub, div, mul

import sys

if __name__ == "__main__":

    arg = sys.argv

    ops = {'+': add, '-': sub, '/': div, '*': mul}

    if len(arg) != 4:

        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if arg[2] not in ops.keys():

        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(arg[1])
    b = int(arg[3])

    print("{} {} {} = {}".format(a, arg[2], b, ops[arg[2]](a, b)))
