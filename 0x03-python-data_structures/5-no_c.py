#!/usr/bin/python3

def no_c(my_string):

    for i, ele in enumerate(my_string):

        if ele == 'c' or ele == 'C':
           my_string = my_string[:i] + '' + my_string[i + 1:]

    return my_string
