#!/usr/bin/python3
"""
Module: 2-post_email.py
"""
from urllib import request
from sys import argv

if __name__ == "__main__":
    url ="{}?email={}".format(argv[1], argv[2])
    with request.urlopen(url) as resp:
        data = resp.read()
        print(data.decode('utf-8'))
