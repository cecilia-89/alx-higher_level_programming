#!/usr/bin/python3

"""Module: def text_indentation()
   Function: def text_indentation(text)
"""


def text_indentation(text):
    """
    Prints string with two additional lines
    after a set of symbols
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    symbols = ['.', ':', '?']

    for count, char in enumerate(text):

        res = char in symbols

        if char == " " and text[count-1] in symbols:
            continue

        print(char, end="" if not res else "\n")

    print()
