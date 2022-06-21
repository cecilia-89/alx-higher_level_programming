#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    count = 0

    for i in range(x):

        num = my_list[i]

        try:
            print("{:d}".format(num), end='')

            count += 1

        except:
            print(end='')

    print()
    return count
