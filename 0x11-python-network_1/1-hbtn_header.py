#!/usr/bin/python3
"""
Module: 1-hbtn_header.py
"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as resp:
        print(resp.headers.get("X-Request-Id"))
