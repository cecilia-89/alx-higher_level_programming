#!/usr/bin/python3
import requests
from sys import argv
"""
Module: 5-hbtn_header.py
"""

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers["X-Request-Id"])
