#!/usr/bin/python3

"""
write_file: opens and reads a file
"""


def append_write(filename="", text=""):

    """
    opens and writes to a file
    """

    with open(filename, 'a', encoding='utf-8') as f:

        append_file = f.write(text)

    return append_file
