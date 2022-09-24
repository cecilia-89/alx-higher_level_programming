#!/usr/bin/python3
"""
Module: 5-hbtn_header.py
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    try:
        print(r.headers["X-Request-Id"])
    except KeyError as err:
        print()
