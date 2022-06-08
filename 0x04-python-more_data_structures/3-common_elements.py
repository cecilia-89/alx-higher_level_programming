#!/usr/bin/python3

def common_elements(set_1, set_2):

    new_lst = set()

    for _str in set_1:

        if _str in set_2:

            new_lst.add(_str)

    return new_lst
