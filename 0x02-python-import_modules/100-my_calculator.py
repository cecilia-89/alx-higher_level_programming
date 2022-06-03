#!/usr/bin/python3

from calculator_1 import add, sub, div, mul

import sys

if __name__ == "__main__":

    arg = sys.argv

    operators = ['+', '-', '/', '*']

    if len(arg) != 3:

        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if arg[2] not in operators:

        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    a = int(arg[1])
    b = int(arg[3])

    if arg[2] == '+':
        print("{} {} {} = {}".format(a, arg[2], b, add(a, b)))

    elif arg[2] == '-':
        print("{} {} {} = {}".format(a, arg[2], b, sub(a, b)))

    elif arg[2] == '/':
        print("{} {} {} = {}".format(a, arg[2], b, div(a, b)))

    else:
        print("{} {} {} = {}".format(a, arg[2], b, mul(a, b)))