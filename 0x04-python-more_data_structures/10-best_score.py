#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary:
        max_num = list(a_dictionary.values())[0]

        for key, value in a_dictionary.items():
            if value > max_num:
                name, max_num = key, value

        return name
