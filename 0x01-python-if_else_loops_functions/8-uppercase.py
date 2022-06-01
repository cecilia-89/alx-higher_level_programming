#!/usr/bin/python3

def uppercase(str):

    for element in str:
        num = ord(element)

        if num > 96 and num < 128:

            num -= 32

            element = chr(num)

        print("{}".format(element), end='')

    print(sep='')
