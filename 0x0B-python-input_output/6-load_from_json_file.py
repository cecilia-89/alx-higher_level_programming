#!/usr/bin/python3
"""
write_file: opens and reads a file
"""

import json


def load_from_json_file(filename):

    """
    opens and writes to a file
    """

    with open(filename, encoding='utf-8') as f:

        json.loads(filename)
