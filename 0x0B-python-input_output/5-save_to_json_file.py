#!/usr/bin/python3
"""
write_file: opens and reads a file
"""
import json


def save_to_json_file(my_obj, filename):

    """
    opens and writes to a file
    """

    with open(filename, 'w', encoding='utf-8') as f:

        json.dump(my_obj, f)
