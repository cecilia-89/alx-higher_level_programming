#!/usr/bin/python3
"""
Module: 2-post_email.py
"""

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    param = {'email': argv[2]}
    query_string = parse.urlencode(param)
    data = query_string.encode("ascii")
    with request.urlopen(argv[1], data) as r:
        data = r.read()
        print(data.decode())
