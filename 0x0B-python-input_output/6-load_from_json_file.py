#!/usr/bin/python3
import json

"""
write_file: opens and reads a file
"""


def load_from_json_file(filename):

    """
    opens and writes to a file
    """

    with open(filename, encoding='utf-8') as f:

        json.loads(filename)
