#!/usr/bin/python3

"""
read_file: opens and reads a file
"""


def read_file(filename=""):

    """
    opens and reads a file
    """

    with open(filename, encoding='utf-8') as f:

        read_file = f.read()
