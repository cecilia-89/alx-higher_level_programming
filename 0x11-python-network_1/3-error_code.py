#!/usr/bin/python3
from urllib import request, error
from sys import argv
"""
Module: 2-post_email.py
"""

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as resp:
            data = resp.read()
            print(data.encode('utf-8'))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")

