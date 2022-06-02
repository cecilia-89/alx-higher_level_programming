#!/usr/bin/python3

import sys

if __name__ == '__main__':

    arglen = len(sys.argv)

    result = 0

    for i in range(1, arglen):

        result += int(sys.argv[i])

    print(result)
