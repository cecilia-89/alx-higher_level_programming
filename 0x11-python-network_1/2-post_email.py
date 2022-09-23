#!/usr/bin/python3
from urllib import request
from sys import argv
"""
Module: 2-post_email.py
"""

if __name__ == "__main__":
    url = f"{argv[1]}?email={argv[2]}"
    with request.urlopen(url) as resp:
        data = resp.read()
        print(data.decode('utf-8'))
