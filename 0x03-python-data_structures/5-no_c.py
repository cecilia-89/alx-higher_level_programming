#!/usr/bin/python3

def no_c(my_string):

    if my_string:

        for i, ele in enumerate(my_string):

            if ele in 'Cc':
                my_string[i] = ''
                ''.join(my_string)

    return my_string
