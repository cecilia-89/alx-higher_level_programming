#!/usr/bin/python3
"""
Module: 3-error_code.py
"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as resp:
            data = resp.read()
            print(data.decode('utf-8'))
    except error.HTTPError as err:
        print(f"Error code: {err.code}")
