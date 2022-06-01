#!/usr/bin/python3

def remove_char_at(str, n):

    if n >= 0 and not n > len(str):

        str_list = list(str)

        str_list[n] = '\0'

        str = ''.join(str_list)

        str.strip

    return str
