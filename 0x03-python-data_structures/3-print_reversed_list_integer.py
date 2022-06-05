#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    
    listlen = len(my_list)

    for i in range(listlen, 0, -1):

        print("{:d}".format(i))
