#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    for count, ele in enumerate(my_list):

        try:
            print(ele, end='')

        except:
            print()

        if count + 1 == x:
            break

    print()
    return count + 1
