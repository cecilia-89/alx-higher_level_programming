#!/usr/bin/python3
"""
Module: 2-post_email.py
"""
import requests
from sys import argv

if __name__ == "__main__":
    data = {'email': argv[2]}
    r = requests.get(argv[1])
    print(r.text)