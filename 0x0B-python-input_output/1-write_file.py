#!/usr/bin/python3

"""
write_file: opens and reads a file
"""


def write_file(filename="", text=""):

    """
    opens and writes to a file
    """

    with open(filename, 'w', encoding='utf-8') as f:

        write_file = f.write(text)

    return write_file
