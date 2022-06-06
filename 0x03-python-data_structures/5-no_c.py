#!/usr/bin/python3

def no_c(my_string):

    if my_string:

        my_string = list(my_string)

        for i, ele in enumerate(my_string):

            if ele in 'Cc':
                my_string[i] = ''

        my_string = ''.join(my_string)

    return my_string
