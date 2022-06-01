#!/usr/bin/python3

def uppercase(str):

    for element in str:
        num = ord(element)


        if num > 96 and num < 128:

            num -= 32

            element = chr(num)

        print(element, end='')

    print(sep='')


uppercase("best")
uppercase("Best School 98 Battery street")
