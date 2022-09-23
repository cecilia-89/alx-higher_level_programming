#!/usr/bin/python3
import requests
from sys import argv
"""
Module: 7-error_code.py
"""

if __name__ == "__main__":

    if len(argv) == 1:
        value = ""
    else:
        value = argv[1]
    data = {'q': value}
    r = requests.get("https://google.com/search", params=data)
    if 'application/json' in r.headers['Content-Type']:
        print('yes')
    else:
        print('no')


