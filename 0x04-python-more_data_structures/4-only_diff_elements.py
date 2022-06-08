#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    uniq_set = set_1.union(set_2)

    for _str in set_1:

        if _str in set_2:

            uniq_set.remove(_str)

    return uniq_set
