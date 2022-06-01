#!/usr/bin/python3

def remove_char_at(str, n):

    if not n > len(str) or n < 0:

        str_list = list(str)

        str_list[n] = '\0'

        str = ''.join(str_list)

    return str
