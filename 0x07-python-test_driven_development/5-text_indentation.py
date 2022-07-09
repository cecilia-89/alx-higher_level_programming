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

    for char in ":?.":

        text = text.replace(char, char + "\n\n")

    res = [string.lstrip() for string in text.split("\n")]

    res = '\n'.join(res)

    print(res)
