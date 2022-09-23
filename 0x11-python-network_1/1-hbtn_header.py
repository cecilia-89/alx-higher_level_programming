#!/usr/bin/python3
from urllib import request
from sys import argv
"""
Module: 1-hbtn_header.py
"""

if __name__ == "__main__":
    with request.urlopen(argv[1]) as resp:
        print(resp.headers.get("X-Request-Id"))
